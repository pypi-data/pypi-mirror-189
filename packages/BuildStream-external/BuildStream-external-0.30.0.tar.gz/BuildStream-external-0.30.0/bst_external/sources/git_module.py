import os

from buildstream import SourceError

from .git_tag import AbstractGitTagSource, GitTagMirror


class GitModuleSource(AbstractGitTagSource):
    # pylint: disable=attribute-defined-outside-init

    BST_FORMAT_VERSION = 2
    BST_REQUIRED_VERSION_MAJOR = 1
    BST_REQUIRED_VERSION_MINOR = 3
    BST_REQUIRES_PREVIOUS_SOURCES_TRACK = True
    BST_REQUIRES_PREVIOUS_SOURCES_FETCH = True

    def get_extra_config_keys(self):
        return ['path']

    def extra_configure(self, node):
        ref = self.node_get_member(node, str, 'ref', '') or None

        self.path = self.node_get_member(node, str, 'path', None)
        if os.path.isabs(self.path):
            self.path = os.path.relpath(self.path, '/')
        self.mirror = GitTagMirror(self, self.path, self.original_url, ref, primary=True, full_clone=self.full_clone)

    def track(self, previous_sources_dir):
        # list objects in the parent repo tree to find the commit
        # object that corresponds to the submodule
        _, output = self.check_output([self.host_git, 'submodule', 'status', self.path],
                                      fail=f"{self}: Failed to run 'git submodule status {self.path}'",
                                      cwd=previous_sources_dir)

        fields = output.split()
        commit = fields[0].lstrip("-+")
        if len(commit) != 40:
            raise SourceError(f"{self}: Unexpected output from 'git submodule status'")

        return commit

    def get_source_fetchers(self):
        yield self.mirror

def setup():
    return GitModuleSource
