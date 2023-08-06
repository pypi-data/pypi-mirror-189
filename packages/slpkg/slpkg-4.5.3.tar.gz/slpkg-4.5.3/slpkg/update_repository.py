#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pathlib import Path
from multiprocessing import Process

from slpkg.configs import Configs
from slpkg.downloader import Downloader
from slpkg.create_data import CreateData
from slpkg.models.models import SBoTable
from slpkg.views.views import ViewMessage
from slpkg.progress_bar import ProgressBar
from slpkg.check_updates import CheckUpdates
from slpkg.models.models import session as Session


class UpdateRepository(Configs):
    """ Deletes and install the data. """

    def __init__(self, flags: list):
        super(Configs, self).__init__()
        self.flags = flags
        self.session = Session
        self.progress = ProgressBar()
        self.color = self.colour()
        self.endc = self.color['endc']

    def sbo(self):
        """ Updated the sbo repository. """
        view = ViewMessage(self.flags)

        view.question()

        print('Updating the package list...\n')
        self.delete_file(self.sbo_repo_path, self.sbo_txt)
        self.delete_file(self.sbo_repo_path, self.sbo_chglog_txt)
        self.delete_sbo_data()

        slackbuilds_txt = f'{self.sbo_repo_url}/{self.sbo_txt}'
        changelog_txt = f'{self.sbo_repo_url}/{self.sbo_chglog_txt}'

        down_slackbuilds = Downloader(self.sbo_repo_path, slackbuilds_txt, self.flags)
        down_slackbuilds.download()

        down_changelog = Downloader(self.sbo_repo_path, changelog_txt, self.flags)
        down_changelog.download()

        data = CreateData()
        data.insert_sbo_table()

    def check(self):
        check_updates = CheckUpdates()
        if not check_updates.check():
            print(f'\n\n{self.endc}No changes in ChangeLog.txt between your last update and now.')
        else:
            print(f'\n\n{self.endc}There are new updates available!')

    def repository(self):
        """ Starting multiprocessing download process. """
        message = f'Checking for news in the Changelog.txt file...'

        # Starting multiprocessing
        p1 = Process(target=self.check)
        p2 = Process(target=self.progress.bar, args=(message, ''))

        p1.start()
        p2.start()

        # Wait until process 1 finish
        p1.join()

        # Terminate process 2 if process 1 finished
        if not p1.is_alive():
            p2.terminate()

        # Wait until process 2 finish
        p2.join()

        # Restore the terminal cursor
        print('\x1b[?25h', self.endc, end='')

        self.sbo()

    @staticmethod
    def delete_file(folder: str, txt_file: str):
        """ Delete the file. """
        file = Path(folder, txt_file)
        if file.exists():
            file.unlink()

    def delete_sbo_data(self):
        """ Delete the table from the database. """
        self.session.query(SBoTable).delete()
        self.session.commit()
