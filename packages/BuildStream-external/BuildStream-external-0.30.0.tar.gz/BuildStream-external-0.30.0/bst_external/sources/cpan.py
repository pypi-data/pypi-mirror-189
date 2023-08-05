#
#  Copyright (C) 2020 Codethink Limited
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

import stat
import zipfile
import contextlib
import codecs
import tarfile
import gzip
import os
import shutil
import urllib.request
from buildstream import Source, SourceError, utils, Consistency


PKG_INDEX = 'modules/02packages.details.txt.gz'
BY_AUTHOR = 'authors/id/'
UTF_CODEC = codecs.lookup('utf-8')


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


class CpanSource(Source):
    def configure(self, node):
        self.node_validate(node, ['url', 'name', 'sha256sum', 'index'] +
                           Source.COMMON_CONFIG_KEYS)

        self.load_ref(node)
        self.name = self.node_get_member(node, str, 'name', None)
        if self.name is None:
            raise SourceError(f'{self}: Missing name')
        self.index = self.node_get_member(node, str, 'index', 'https://cpan.metacpan.org/')
        self.scheme = self.node_get_member(node, list, 'scheme', None)
        if self.scheme is None and self.index == 'https://cpan.metacpan.org/':
            self.scheme = 'cpan'

    def preflight(self):
        pass

    def get_unique_key(self):
        return [self.url, self.sha256sum]

    def load_ref(self, node):
        self.sha256sum = self.node_get_member(node, str, 'sha256sum', None)
        self.url = self.node_get_member(node, str, 'url', None)
        if self.url is not None:
            self.translated_url = self.translate_url(self.url)
        else:
            self.translated_url = None

    def get_ref(self):
        if self.url is None or self.sha256sum is None:
            return None
        return {'url': self.url,
                'sha256sum': self.sha256sum}

    def set_ref(self, ref, node):
        node['url'] = self.url = ref['url']
        node['sha256sum'] = self.sha256sum = ref['sha256sum']

    def track(self):
        found = None
        with urllib.request.urlopen(f'{self.index}{PKG_INDEX}') as response:
            with gzip.GzipFile(fileobj=response) as data:
                listing = UTF_CODEC.streamreader(data)
                while True:
                    line = listing.readline()
                    if not line:
                        break
                    line = line.rstrip('\r\n')
                    if len(line) == 0:
                        break
                while True:
                    line = listing.readline()
                    if not line:
                        break
                    line = line.rstrip('\r\n')
                    package, _, url = line.split()
                    if package == self.name:
                        found = url
                        break
        if not found:
            raise SourceError(f'{self}: "{self.name}" not found in {self.index}')

        if self.scheme:
            self.url = f'{self.scheme}:{BY_AUTHOR}{found}'
        else:
            self.url = f'{self.index}{BY_AUTHOR}{found}'
        self.translated_url = f'{self.index}{BY_AUTHOR}{found}'
        self.sha256sum = self._ensure_sources(validate=False)
        return self.get_ref()

    def _get_mirror_dir(self):
        return os.path.join(self.get_mirror_directory(),
                            utils.url_directory_name(self.name))

    def _get_mirror_file(self, sha=None):
        return os.path.join(self._get_mirror_dir(), sha or self.sha256sum)

    def _ensure_sources(self, validate=True):
        # More or less copied from _downloadablefilesource.py
        try:
            with self.tempdir() as tempdir:
                default_name = os.path.basename(self.translated_url)
                request = urllib.request.Request(self.translated_url)
                request.add_header('Accept', '*/*')
                request.add_header('User-Agent', 'BuildStream/1')

                with contextlib.closing(urllib.request.urlopen(request)) as response:
                    info = response.info()
                    filename = info.get_filename(default_name)
                    filename = os.path.basename(filename)
                    local_file = os.path.join(tempdir, filename)
                    with open(local_file, 'wb') as dest:
                        shutil.copyfileobj(response, dest)

                if not os.path.isdir(self._get_mirror_dir()):
                    os.makedirs(self._get_mirror_dir())

                computed = utils.sha256sum(local_file)
                if validate and self.sha256sum != computed:
                    raise SourceError(
                        f"{self.url} expected hash {self.sha256sum}, got {computed}"
                    )
                os.rename(local_file, self._get_mirror_file(computed))

                return computed

        except (urllib.error.URLError, urllib.error.ContentTooShortError, OSError) as e:
            raise SourceError(f"{self}: Error mirroring {self.translated_url}: {e}",
                              temporary=True) from e

    def fetch(self):
        self._ensure_sources()

    def stage(self, directory):
        if not os.path.exists(self._get_mirror_file()):
            raise SourceError(f"{self}: Cannot find mirror file {self._get_mirror_file()}")
        if self.translated_url.endswith('.zip'):
            with zipfile.ZipFile(self._get_mirror_file(), mode='r') as zipf:
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
            with tarfile.open(self._get_mirror_file(), 'r:gz') as tar:
                tar.extractall(path=directory, members=strip_top_dir(tar.getmembers(), 'path'))

    def get_consistency(self):
        if self.url is None or self.sha256sum is None:
            return Consistency.INCONSISTENT

        if os.path.isfile(self._get_mirror_file()):
            return Consistency.CACHED
        return Consistency.RESOLVED

def setup():
    return CpanSource
