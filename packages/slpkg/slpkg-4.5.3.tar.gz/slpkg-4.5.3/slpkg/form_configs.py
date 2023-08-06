#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

from slpkg.configs import Configs
from slpkg.configs import LoadConfigs
from slpkg.dialog_box import DialogBox


class FormConfigs(Configs):

    def __init__(self):
        self.orig_configs = None
        self.load_configs = LoadConfigs()
        self.dialogbox = DialogBox()
        self.config_file = Path(self.etc_path, f'{self.prog_name}.toml')

    def edit(self):
        """ Read and write the configuration file. """
        elements = []
        config_file = Path(self.etc_path, f'{self.prog_name}.toml')

        if config_file.is_file():
            # Load the toml config file.
            configs = self.load_configs.file(self.etc_path, self.prog_name)

            # Creating the elements for the dialog form.
            for i, (key, value) in enumerate(configs['configs'].items(), start=1):
                if value is True:
                    value = 'true'
                elif value is False:
                    value = 'false'
                elements += [
                    (key, i, 1, value, i, 17, 47, 200, '0x0')
                ]

            height = 28
            width = 70
            text = f'Edit the configuration file: {config_file}'
            title = ' Configuration File '

            code, tags = self.dialogbox.mixedform(text, title, elements, height, width)

            os.system('clear')

            check = self.check_configs(configs, tags)

            if code == 'ok' and check:
                self.write_file(configs, tags)
            elif not check:
                self.edit()
            elif code == 'help':
                self.help()

    def help(self):
        """ Load the configuration file on a text box. """
        self.read_configs()
        self.dialogbox.textbox(str(self.config_file), 40, 60)
        self.edit()

    def check_configs(self, configs: dict, tags: list) -> bool:
        """ Check for true of false values. """
        for key, value in zip(configs['configs'].keys(), tags):

            if key in ['colors', 'dialog', 'silent_mode', 'ascii_characters'] and value not in ['true', 'false']:
                self.dialogbox.msgbox(f"\nError value for {key}. It must be 'true' or 'false'\n", height=7, width=60)
                return False

            if key in ['downloader'] and value not in ['wget', 'curl']:
                self.dialogbox.msgbox(f"\nError value for {key}. It must be 'wget' or 'curl'\n", height=7, width=60)
                return False

        return True

    def read_configs(self):
        """ Read the original config file. """
        with open(self.config_file, 'r') as toml_file:
            self.orig_configs = toml_file.readlines()

    def write_file(self, configs: dict, tags: list):
        """ Write the new values to the config file. """
        self.read_configs()
        with open(self.config_file, 'w') as patch_toml:
            for line in self.orig_configs:
                for key, value in zip(configs['configs'].keys(), tags):
                    if line.lstrip().startswith(key):
                        line = f'  {key} = "{value}"\n'
                    if line.lstrip().startswith(('colors =', 'dialog =', 'silent_mode =', 'ascii_characters =')):
                        line = line.replace('"', '')
                patch_toml.write(line)
