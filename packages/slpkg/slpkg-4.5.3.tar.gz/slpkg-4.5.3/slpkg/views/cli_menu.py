#!/usr/bin/python3
# -*- coding: utf-8 -*-

from slpkg.configs import Configs


class Usage(Configs):

    def __init__(self):
        super(Configs, self).__init__()
        color = self.colour()

        self.bold = color['bold']
        self.red = color['red']
        self.cyan = color['cyan']
        self.yellow = color['yellow']
        self.endc = color['endc']

    def help_short(self):
        """ Prints the short menu. """
        args = (
            f'Usage: {Configs.prog_name} [{self.yellow}OPTIONS{self.endc}] [{self.cyan}COMMAND{self.endc}] <packages>\n'
            f'\n  slpkg [{self.cyan}COMMAND{self.endc}] [-u, update, -U, upgrade, -c, check-updates]\n'
            f'  slpkg [{self.cyan}COMMAND{self.endc}] [-L, clean-logs, -D, clean-tmp, -g, configs]\n'
            f'  slpkg [{self.cyan}COMMAND{self.endc}] [-b, build, -i, install, -d, download, -r, remove] <packages>\n'
            f'  slpkg [{self.cyan}COMMAND{self.endc}] [-f, find, -w, view, -s, search] <packages>\n'
            f'  slpkg [{self.cyan}COMMAND{self.endc}] [-e, dependees, -t, tracking] <packages>\n'
            f'  slpkg [{self.yellow}OPTIONS{self.endc}] [-y, --yes, -j, --jobs, -ro, --resolve-off, -R, --reinstall]\n'
            f'  slpkg [{self.yellow}OPTIONS{self.endc}] [-si, --skip-installed, -fr, --full-reverse, -S, --search]\n'
            f'  slpkg [{self.yellow}OPTIONS{self.endc}] [-ns, --no-silent, -dir=, --directory=PATH]\n'
            f'  slpkg [{self.yellow}OPTIONS{self.endc}] [-pv, --pkg-version, -fp=, --file-pattern=PATTERN]\n'
            "  \nIf you need more information please try 'slpkg --help'.")

        print(args)
        raise SystemExit()

    def help(self, status: int):
        """ Prints the main menu. """
        args = (
            f'{self.bold}USAGE:{self.endc} {Configs.prog_name} [{self.yellow}OPTIONS{self.endc}] '
            f'[{self.cyan}COMMAND{self.endc}] <packages>\n'
            f'\n{self.bold}DESCRIPTION:{self.endc} Packaging tool that interacts with the SBo repository.\n'
            f'\n{self.bold}COMMANDS:{self.endc}\n'
            f'  {self.red}-u, update{self.endc}                    Update the package lists.\n'
            f'  {self.cyan}-U, upgrade{self.endc}                   Upgrade all the packages.\n'
            f'  {self.cyan}-c, check-updates{self.endc}             Check for news on ChangeLog.txt.\n'
            f'  {self.cyan}-g, configs{self.endc}                   Edit the configuration file.\n'
            f'  {self.cyan}-L, clean-logs{self.endc}                Clean dependencies log tracking.\n'
            f'  {self.cyan}-D, clean-tmp{self.endc}                 Delete all the downloaded sources.\n'
            f'  {self.cyan}-b, build{self.endc} <packages>          Build only the packages.\n'
            f'  {self.cyan}-i, install{self.endc} <packages>        Build and install the packages.\n'
            f'  {self.cyan}-d, download{self.endc} <packages>       Download only the scripts and sources.\n'
            f'  {self.cyan}-r, remove{self.endc} <packages>         Remove installed packages.\n'
            f'  {self.cyan}-f, find{self.endc} <packages>           Find installed packages.\n'
            f'  {self.cyan}-w, view{self.endc} <packages>           View packages from the repository.\n'
            f'  {self.cyan}-s, search{self.endc} <packages>         Search packages from the repository.\n'
            f'  {self.cyan}-e, dependees{self.endc} <packages>      Show which packages depend.\n'
            f'  {self.cyan}-t, tracking{self.endc} <packages>       Tracking the packages dependencies.\n'
            f'\n{self.bold}OPTIONS:{self.endc}\n'
            f'  {self.yellow}-y, --yes{self.endc}                     Answer Yes to all questions.\n'
            f'  {self.yellow}-j, --jobs{self.endc}                    Set it for multicore systems.\n'
            f'  {self.yellow}-ro, --resolve-off{self.endc}            Turns off dependency resolving.\n'
            f'  {self.yellow}-R, --reinstall{self.endc}               Upgrade packages of the same version.\n'
            f'  {self.yellow}-si, --skip-installed{self.endc}         Skip installed packages.\n'
            f'  {self.yellow}-fr, --full-reverse{self.endc}           Full reverse dependency.\n'
            f'  {self.yellow}-S, --search{self.endc}                  Search packages from the repository.\n'
            f'  {self.yellow}-ns, --no-silent{self.endc}              Disable silent mode.\n'
            f'  {self.yellow}-dir=, --directory={self.endc}PATH       Download files to a specific path.\n'
            f'  {self.yellow}-pv, --pkg-version{self.endc}            Print the repository package version.\n'
            f'  {self.yellow}-fp=, --file-pattern={self.endc}PATTERN  Include specific installed files.\n'
            '\n  -h, --help                    Show this message and exit.\n'
            '  -v, --version                 Print version and exit.\n'
            '\nEdit the configuration file in the /etc/slpkg/slpkg.toml \n'
            "or run 'slpkg configs'.\n"
            'If you need more information try to use slpkg manpage.')

        print(args)
        raise SystemExit(status)

    def error_for_options(self, flags):
        """ Error messages for flags. """
        print(f'Usage: {Configs.prog_name} [{self.yellow}OPTIONS{self.endc}] '
              f'[{self.cyan}COMMAND{self.endc}] <packages>')
        print("Try 'slpkg --help' for help.\n")
        if flags:
            raise SystemExit(f"{self.red}Error:{self.endc} Got an unexpected extra option, "
                             f"please use: \n{self.yellow}'{', '.join(flags)}'{self.endc}")

        raise SystemExit(f"{self.red}Error:{self.endc} Got an unexpected extra option.")
