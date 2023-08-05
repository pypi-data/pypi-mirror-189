#
#  Copyright (C) 2020 Codethink Limited
#  Copyright (C) 2020-2022 Seppo Yli-Olli
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library. If not, see <http://www.gnu.org/licenses/>.
#
#  Authors:
#         Valentin David <valentin.david@codethink.co.uk>
#         Seppo Yli-Olli <seppo.yli-olli@iki.fi>

import os
import os.path
import re
import shutil
import tarfile
import zipfile
import stat
import contextlib
import urllib.request
import urllib.parse
import json
from datetime import datetime
from buildstream import Source, SourceError, utils, Consistency, SourceFetcher


def strip_top_dir(members, attr):
    for member in members:
        path = getattr(member, attr)
        trail_slash = path.endswith('/')
        path = path.rstrip('/')
        splitted = getattr(member, attr).split('/', 1)
        if len(splitted) == 2:
            new_path = splitted[1]
            if trail_slash:
                new_path += '/'
            setattr(member, attr, new_path)
            yield member

def make_key(item):
    for download in item[1]:
        if download['packagetype'] == 'sdist':
            try:
                date = datetime.strptime(download['upload_time_iso_8601'],
                                         '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError:
                date = datetime.strptime(download['upload_time_iso_8601'],
                                             '%Y-%m-%dT%H:%M:%SZ')
            return date
    return datetime.fromtimestamp(0)


class Downloader(SourceFetcher):
    def __init__(self, source, name):
        self.source = source
        self.mark_download_url(self.source.base_url)
        self.mirror_directory = os.path.join(
            self.source.get_mirror_directory(),
            utils.url_directory_name(name)
        )

    @property
    def mirror_file(self):
        return os.path.join(self.mirror_directory, self.source.sha256sum)

    def fetch(self, alias_override=None):
        base_url = self.source.translate_url(self.source.base_url,
                                             alias_override=alias_override)
        url = base_url + self.source.suffix
        # Loosely based on _downloadablefilesource.py

        with contextlib.ExitStack() as stack:
            stack.enter_context(self.source.timed_activity(
                "Fetching from {}".format(url)
            ))

            try:
                tempdir = stack.enter_context(self.source.tempdir())
                default_name = os.path.basename(url)
                request = urllib.request.Request(url)
                request.add_header('Accept', '*/*')
                request.add_header('User-Agent', 'BuildStream/1')

                response = stack.enter_context(urllib.request.urlopen(request))
                info = response.info()
                filename = info.get_filename(default_name)
                filename = os.path.basename(filename)
                local_file = os.path.join(tempdir, filename)

                with open(local_file, 'wb') as dest:
                    shutil.copyfileobj(response, dest)
                response.close()

                os.makedirs(self.mirror_directory, exist_ok=True)

                sha256 = self.source.sha256sum
                computed = utils.sha256sum(local_file)
                if sha256 != computed:
                    raise SourceError(f"{url} expected hash {sha256}, got {computed}")
                os.rename(local_file, self.mirror_file)
                return sha256

            except (
                    urllib.error.URLError,
                    urllib.error.ContentTooShortError, OSError
            ) as e:
                raise SourceError(f"{self}: Error mirroring {url}: {e}",
                                  temporary=True) from e

class PyPISource(Source):
    REST_API = "https://pypi.org/pypi/{name}/json"
    STORAGE_ROOT = "https://files.pythonhosted.org/packages/"
    KEYS = [
        "url",
        "name",
        "ref",
        "include",
        "exclude",
    ] + Source.COMMON_CONFIG_KEYS

    def configure(self, node):
        self.node_validate(node, self.KEYS)

        self.name = self.node_get_member(node, str, 'name')

        self.suffix = self.sha256sum = None

        self.include = self.node_get_member(node, list, 'include', [])
        self.exclude = self.node_get_member(node, list, 'exclude', [])

        self.base_url = self.node_get_member(
            node,
            str,
            "url",
            self.STORAGE_ROOT,
        )
        self.mark_download_url(self.base_url)
        self.fetcher = Downloader(
            self,
            self.name
        )
        self.load_ref(node)

    def preflight(self):
        pass

    @property
    def url(self):
        if self.suffix:
            return self.translate_url(self.base_url) + self.suffix

    @property
    def original_url(self):
        if self.suffix:
            return self.base_url + self.suffix

    def get_unique_key(self):
        ref = self.get_ref()
        return [
            ref["suffix"],
            ref["sha256sum"]
        ]

    def load_ref(self, node):
        ref = self.node_get_member(node, dict, "ref", None)
        if ref:
            self.node_validate(ref, ["sha256sum", "suffix"])
            self.set_ref(ref, node)

    def get_ref(self):
        if self.suffix and self.sha256sum:
            return {
                "sha256sum": self.sha256sum,
                "suffix": self.suffix,
            }
        return None

    def set_ref(self, ref, node):
        if ref is None:
            self.suffix = self.sha256sum = None
        else:
            self.suffix = ref["suffix"]
            self.sha256sum = ref["sha256sum"]
        node["ref"] = ref

    def track(self):
        payload = json.loads(
            urllib.request.urlopen(self.REST_API.format(name=self.name)).read()
        )
        releases = payload['releases']
        if not releases:
            raise SourceError(f'{self}: Cannot find any tracking for {self.name}')
        selected_release = None
        if self.include or self.exclude:
            includes = list(map(re.compile, self.include))
            excludes = list(map(re.compile, self.exclude))
            urls = self._calculate_latest(releases,
                                          includes,
                                          excludes
                                          )
        else:
            urls = releases[payload['info']['version']]
        found_ref = None
        for url in urls:
            if url['packagetype'] == 'sdist':
                found_ref = {
                    'sha256sum': url['digests']['sha256'],
                    'suffix': url['url'].replace(self.STORAGE_ROOT, ""),
                }
                break

        if found_ref is None:
            raise SourceError(f'{self}: Did not find any sdist for {self.name} {selected_release}')

        return found_ref

    def get_source_fetchers(self):
        return [self.fetcher]

    def _calculate_latest(self, releases, includes, excludes):
        for release, urls in sorted(releases.items(), key=make_key, reverse=True):
            if excludes:
                excluded = False
                for exclude in excludes:
                    if exclude.match(release):
                        excluded = True
                        break
                if excluded:
                    continue
            if includes:
                for include in includes:
                    if include.match(release):
                        return urls
            else:
                return urls

        raise SourceError(f'{self}: No matching release')

    def stage(self, directory):
        if not os.path.exists(self.fetcher.mirror_file):
            raise SourceError(f"{self}: Cannot find mirror file {self.fetcher.mirror_file}")
        if self.suffix.endswith('.zip'):
            with zipfile.ZipFile(self.fetcher.mirror_file, mode='r') as zipf:
                exec_rights = (stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO) & ~(stat.S_IWGRP | stat.S_IWOTH)
                noexec_rights = exec_rights & ~(stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                # Taken from zip plugin. It is needed to ensure reproducibility of permissions
                for member in strip_top_dir(zipf.infolist(), 'filename'):
                    written = zipf.extract(member, path=directory)
                    rel = os.path.relpath(written, start=directory)
                    assert not os.path.isabs(rel)
                    rel = os.path.dirname(rel)
                    while rel:
                        os.chmod(os.path.join(directory, rel), exec_rights)
                        rel = os.path.dirname(rel)

                    if os.path.islink(written):
                        pass
                    elif os.path.isdir(written):
                        os.chmod(written, exec_rights)
                    else:
                        os.chmod(written, noexec_rights)
        else:
            with tarfile.open(self.fetcher.mirror_file, 'r:gz') as tar:
                tar.extractall(path=directory, members=strip_top_dir(tar.getmembers(), 'path'))

    def get_consistency(self):
        if self.get_ref() is None:
            return Consistency.INCONSISTENT
        if os.path.isfile(self.fetcher.mirror_file):
            return Consistency.CACHED
        return Consistency.RESOLVED

def setup():
    return PyPISource
