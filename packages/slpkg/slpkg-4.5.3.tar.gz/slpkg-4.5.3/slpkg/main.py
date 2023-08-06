#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from slpkg.checks import Check
from slpkg.upgrade import Upgrade
from slpkg.configs import Configs
from slpkg.tracking import Tracking
from slpkg.queries import SBoQueries
from slpkg.dependees import Dependees
from slpkg.utilities import Utilities
from slpkg.search import SearchPackage
from slpkg.views.cli_menu import Usage
from slpkg.dialog_box import DialogBox
from slpkg.views.version import Version
from slpkg.download_only import Download
from slpkg.slackbuild import Slackbuilds
from slpkg.form_configs import FormConfigs
from slpkg.check_updates import CheckUpdates
from slpkg.find_installed import FindInstalled
from slpkg.views.view_package import ViewPackage
from slpkg.remove_packages import RemovePackages
from slpkg.clean_logs import CleanLogsDependencies
from slpkg.update_repository import UpdateRepository


class Argparse(Configs):

    def __init__(self, args: list):
        self.args = args
        self.flags = []
        self.directory = None
        self.file_pattern = f'*{self.sbo_repo_tag}'
        self.dialogbox = DialogBox()
        self.utils = Utilities()
        self.usage = Usage()
        self.check = Check()
        self.form_configs = FormConfigs()

        if len(self.args) == 0:
            self.usage.help_short()

        self.check.blacklist(self.args)

        self.flag_yes = '--yes'
        self.flag_short_yes = '-y'
        self.flag_jobs = '--jobs'
        self.flag_short_jobs = '-j'
        self.flag_resolve_off = '--resolve-off'
        self.flag_short_resolve_off = '-ro'
        self.flag_reinstall = '--reinstall'
        self.flag_short_reinstall = '-R'
        self.flag_skip_installed = '--skip-installed'
        self.flag_short_skip_installed = '-si'
        self.flag_full_reverse = '--full-reverse'
        self.flag_short_full_reverse = '-fr'
        self.flag_search = '--search'
        self.flag_short_search = '-S'
        self.flag_no_silent = '--no-silent'
        self.flag_short_no_silent = '-ns'
        self.flag_directory = '--directory='
        self.flag_short_directory = '-dir='
        self.flag_pkg_version = '--pkg-version'
        self.flag_short_pkg_version = '-pv'
        self.flag_file_pattern = '--file-pattern='
        self.flag_short_file_pattern = '-fp='

        self.flag_searches = [self.flag_short_search, self.flag_search]

        self.is_dialog_enabled()

        self.options = [self.flag_yes,
                        self.flag_short_yes,
                        self.flag_jobs,
                        self.flag_short_jobs,
                        self.flag_resolve_off,
                        self.flag_short_resolve_off,
                        self.flag_reinstall,
                        self.flag_short_reinstall,
                        self.flag_skip_installed,
                        self.flag_short_skip_installed,
                        self.flag_full_reverse,
                        self.flag_short_full_reverse,
                        self.flag_search,
                        self.flag_short_search,
                        self.flag_no_silent,
                        self.flag_short_no_silent,
                        self.flag_directory,
                        self.flag_short_directory,
                        self.flag_pkg_version,
                        self.flag_short_pkg_version,
                        self.flag_file_pattern,
                        self.flag_short_file_pattern]

        self.remove_flags()

    def remove_flags(self):
        """ Remove flags from args. """
        for arg in self.args:
            if arg.startswith(self.flag_directory):
                self.directory = arg.split('=')[1]
                self.args[self.args.index(arg)] = self.flag_directory

            if arg.startswith(self.flag_short_directory):
                self.directory = arg.split('=')[1]
                self.args[self.args.index(arg)] = self.flag_directory

            if arg.startswith(self.flag_file_pattern):
                self.file_pattern = arg.split('=')[1]
                self.args[self.args.index(arg)] = self.flag_file_pattern

            if arg.startswith(self.flag_short_file_pattern):
                self.file_pattern = arg.split('=')[1]
                self.args[self.args.index(arg)] = self.flag_file_pattern

        for opt in self.options:
            if opt in self.args:
                self.args.remove(opt)
                self.flags.append(opt)

    def is_dialog_enabled(self):
        """ Checking if the dialog box is enabled. """
        if (not self.dialogbox and self.utils.is_option(self.flag_searches, self.flags) or
                not self.dialogbox.dialog and 'configs' in self.args):
            raise SystemExit("\nError: You should enable the dialog "
                             "in the '/etc/slpkg/' folder.\n")

    def check_for_flags(self, command: str):
        """ Check for correct flags. """

        commands = {
            '--help': [],
            '--version': [],
            'update': [
                self.flag_yes,
                self.flag_short_yes,
                self.flag_no_silent,
                self.flag_short_no_silent
            ],
            'upgrade': [
                self.flag_yes,
                self.flag_jobs,
                self.flag_short_jobs,
                self.flag_resolve_off,
                self.flag_short_resolve_off,
                self.flag_reinstall,
                self.flag_short_reinstall,
                self.flag_no_silent,
                self.flag_short_no_silent,
                self.flag_file_pattern,
                self.flag_short_file_pattern
            ],
            'check-updates': [],
            'configs': [],
            'clean-logs': [self.flag_yes],
            'clean-tmp': [],
            'build': [
                self.flag_yes,
                self.flag_short_yes,
                self.flag_jobs,
                self.flag_short_jobs,
                self.flag_resolve_off,
                self.flag_short_resolve_off,
                self.flag_search,
                self.flag_short_search,
                self.flag_no_silent,
                self.flag_short_no_silent
            ],
            'install': [
                self.flag_yes,
                self.flag_short_yes,
                self.flag_jobs,
                self.flag_short_jobs,
                self.flag_resolve_off,
                self.flag_short_resolve_off,
                self.flag_reinstall,
                self.flag_short_reinstall,
                self.flag_skip_installed,
                self.flag_short_skip_installed,
                self.flag_search,
                self.flag_short_search,
                self.flag_no_silent,
                self.flag_short_no_silent,
                self.flag_file_pattern,
                self.flag_short_file_pattern
            ],
            'download': [
                self.flag_yes,
                self.flag_short_yes,
                self.flag_search,
                self.flag_short_search,
                self.flag_no_silent,
                self.flag_short_no_silent,
                self.flag_directory,
                self.flag_short_directory
            ],
            'remove': [
                self.flag_yes,
                self.flag_short_yes,
                self.flag_resolve_off,
                self.flag_short_resolve_off,
                self.flag_search,
                self.flag_short_search,
                self.flag_no_silent,
                self.flag_short_no_silent,
                self.flag_file_pattern,
                self.flag_short_file_pattern
            ],
            'find': [
                self.flag_search,
                self.flag_short_search,
                self.flag_file_pattern,
                self.flag_short_file_pattern
            ],
            'view': [
                self.flag_search,
                self.flag_short_search,
                self.flag_pkg_version,
                self.flag_short_pkg_version
            ],
            'search': [
                self.flag_search,
                self.flag_short_search,
            ],
            'dependees': [
                self.flag_full_reverse,
                self.flag_short_full_reverse,
                self.flag_search,
                self.flag_short_search,
                self.flag_pkg_version,
                self.flag_short_pkg_version
            ],
            'tracking': [
                self.flag_search,
                self.flag_short_search,
                self.flag_pkg_version,
                self.flag_short_pkg_version
            ]
        }

        commands['-h'] = commands['--help']
        commands['-v'] = commands['--version']
        commands['-u'] = commands['update']
        commands['-U'] = commands['upgrade']
        commands['-c'] = commands['check-updates']
        commands['-g'] = commands['configs']
        commands['-L'] = commands['clean-logs']
        commands['-D'] = commands['clean-tmp']
        commands['-b'] = commands['build']
        commands['-i'] = commands['install']
        commands['-d'] = commands['download']
        commands['-r'] = commands['remove']
        commands['-f'] = commands['find']
        commands['-w'] = commands['view']
        commands['-s'] = commands['search']
        commands['-e'] = commands['dependees']
        commands['-t'] = commands['tracking']

        flags = commands[command]

        for opt in self.flags:
            if opt not in flags and opt not in ['--help', '--version']:
                self.usage.error_for_options(flags)

    def choose_packages(self, packages: list, method: str):
        """ Choose packages with dialog utility and -S, --search flag. """
        height = 10
        width = 70
        list_height = 0
        choices = []
        title = f' Choose packages you want to {method} '
        repo_packages = SBoQueries('').sbos()

        # Grab all the installed packages
        pattern = f'*{self.sbo_repo_tag}'

        if method == 'find' and self.file_pattern:
            pattern = self.file_pattern

        installed = self.utils.all_installed(pattern)

        if method in ['remove', 'find']:

            for package in installed:
                name = self.utils.split_installed_pkg(package)[0]
                version = self.utils.split_installed_pkg(package)[1]

                for pkg in packages:
                    if pkg in name:
                        choices += [(name, version, False)]

        elif method == 'upgrade':
            for pkg in packages:
                for package in repo_packages:

                    if pkg == package:
                        repo_ver = SBoQueries(package).version()
                        inst_pkg = self.utils.is_installed(package, self.file_pattern)
                        inst_ver = self.utils.split_installed_pkg(inst_pkg)[1]
                        choices += [(package, f'{inst_ver} -> {repo_ver}', True)]

        else:
            for pkg in packages:
                for package in repo_packages:

                    if pkg in package:
                        repo_ver = SBoQueries(package).version()
                        choices += [(package, repo_ver, False)]

        if not choices:
            return packages

        text = f'There are {len(choices)} packages:'

        code, tags = self.dialogbox.checklist(text, title, height, width,
                                              list_height, choices, packages)

        if not code:
            return packages

        os.system('clear')

        if not tags:
            raise SystemExit()

        return tags

    def help(self):
        if len(self.args) == 1:
            self.usage.help(0)
        self.usage.help(1)

    def version(self):
        if len(self.args) == 1:
            version = Version()
            version.view()
            raise SystemExit()
        self.usage.help(1)

    def update(self):
        if len(self.args) == 1:
            update = UpdateRepository(self.flags)
            update.repository()
            raise SystemExit()
        self.usage.help(1)

    def upgrade(self):
        command = Argparse.upgrade.__name__

        if len(self.args) == 1:
            self.check.database()

            upgrade = Upgrade(self.file_pattern)
            packages = list(upgrade.packages())

            packages = self.choose_packages(packages, command)

            if not packages:
                print('\nEverything is up-to-date.\n')
                raise SystemExit()

            install = Slackbuilds(packages, self.flags, self.file_pattern, mode=command)
            install.execute()
            raise SystemExit()
        self.usage.help(1)

    def check_updates(self):
        if len(self.args) == 1:
            self.check.database()

            check = CheckUpdates()
            check.updates()
            raise SystemExit()
        self.usage.help(1)

    def edit_configs(self):
        if len(self.args) == 1:
            self.form_configs.edit()
            raise SystemExit()
        self.usage.help(1)

    def clean_logs(self):
        if len(self.args) == 1:
            self.check.database()

            logs = CleanLogsDependencies(self.flags)
            logs.clean()
            raise SystemExit()
        self.usage.help(1)

    def clean_tmp(self):
        if len(self.args) == 1:
            path = self.tmp_path
            tmp_slpkg = self.tmp_slpkg
            folder = self.prog_name

            self.utils.remove_folder_if_exists(path, folder)
            self.utils.create_folder(tmp_slpkg, 'build')
            raise SystemExit()
        self.usage.help(1)

    def build(self):
        command = Argparse.build.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()
            self.check.exists(packages)
            self.check.unsupported(packages)

            build = Slackbuilds(packages, self.flags, self.file_pattern, mode=command)
            build.execute()
            raise SystemExit()
        self.usage.help(1)

    def install(self):
        command = Argparse.install.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()
            self.check.exists(packages)
            self.check.unsupported(packages)

            install = Slackbuilds(packages, self.flags, self.file_pattern, mode=command)
            install.execute()
            raise SystemExit()
        self.usage.help(1)

    def download(self):
        command = Argparse.download.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()
            self.check.exists(packages)
            download = Download(self.directory, self.flags)
            download.packages(packages)
            raise SystemExit()
        self.usage.help(1)

    def remove(self):
        command = Argparse.remove.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()
            packages = self.check.installed(packages, self.file_pattern)

            remove = RemovePackages(packages, self.flags, self.file_pattern)
            remove.remove()
            raise SystemExit()
        self.usage.help(1)

    def find(self):
        command = Argparse.find.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()

            find = FindInstalled()
            find.find(packages, self.file_pattern)
            raise SystemExit()
        self.usage.help(1)

    def view(self):
        command = Argparse.view.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()
            self.check.exists(packages)

            view = ViewPackage(self.flags)
            view.package(packages)
            raise SystemExit()
        self.usage.help(1)

    def search(self):
        command = Argparse.search.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()

            search = SearchPackage()
            search.package(packages)
            raise SystemExit()
        self.usage.help(1)

    def dependees(self):
        command = Argparse.dependees.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()
            self.check.exists(packages)

            dependees = Dependees(packages, self.flags)
            dependees.slackbuilds()
            raise SystemExit()
        self.usage.help(1)

    def tracking(self):
        command = Argparse.tracking.__name__

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if self.utils.is_option(self.flag_searches, self.flags):
                packages = self.choose_packages(packages, command)

            self.check.database()
            self.check.exists(packages)

            tracking = Tracking(self.flags)
            tracking.packages(packages)
            raise SystemExit()
        self.usage.help(1)


def main():
    args = sys.argv
    args.pop(0)

    argparse = Argparse(args)

    arguments = {
        '-h': argparse.help,
        '--help': argparse.help,
        '-v': argparse.version,
        '--version': argparse.version,
        'update': argparse.update,
        '-u': argparse.update,
        'upgrade': argparse.upgrade,
        '-U': argparse.upgrade,
        'check-updates': argparse.check_updates,
        '-c': argparse.check_updates,
        'configs': argparse.edit_configs,
        '-g': argparse.edit_configs,
        'clean-logs': argparse.clean_logs,
        '-L': argparse.clean_logs,
        'clean-tmp': argparse.clean_tmp,
        '-D': argparse.clean_tmp,
        'build': argparse.build,
        '-b': argparse.build,
        'install': argparse.install,
        '-i': argparse.install,
        'download': argparse.download,
        '-d': argparse.download,
        'remove': argparse.remove,
        '-r': argparse.remove,
        'view': argparse.view,
        '-w': argparse.view,
        'find': argparse.find,
        '-f': argparse.find,
        'search': argparse.search,
        '-s': argparse.search,
        'dependees': argparse.dependees,
        '-e': argparse.dependees,
        'tracking': argparse.tracking,
        '-t': argparse.tracking
    }

    try:
        argparse.check_for_flags(args[0])
        arguments[args[0]]()
    except (KeyError, IndexError):
        Usage().help(1)


if __name__ == '__main__':
    main()
