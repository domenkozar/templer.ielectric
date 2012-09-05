# -*- coding: utf-8 -*-
""" Script for upgrading database with Alembic."""

import argparse
import os
import sys
from datetime import date

from alembic.command import upgrade
from alembic.config import Config


class MigrateDatabaseCommand(object):
    """ Upgrade the database using the configuration from the .ini file passed
    as a positional argument.
    """
    description = 'Upgrade the database'
    usage = '%(prog)s config_uri'
    epilog = 'example: %(prog)s development.ini'

    parser = argparse.ArgumentParser(
        description=description,
        usage=usage,
        epilog=epilog)
    parser.add_argument('config_uri', nargs='?',
                        help='the application config file')

    def __init__(self, argv):
        """ Get arguments from the ``argparse`` parser."""
        self.args = self.parser.parse_args(argv)

    def run(self):
        """ Run the ``migrate`` method or display the parser help message
        if the `config_uri` argument is missing.

        :return: `0 (OK) or 1 (abnormal termination error) or 2 (missing argument error)
        """
        if not self.args.config_uri:
            self.parser.print_help()
            return 2
        else:
            return self.migrate()

    def migrate(self):
        """ Upgrade the database to the head revision with Alembic.

        :return: 0 (OK) or 1 (abnormal termination error)
        """
        config_uri = self.args.config_uri
        alembic_config = get_alembic_settings(config_uri)

        upgrade(alembic_config, 'head')

        print("Database upgrade done.")
        return 0


def get_alembic_settings(config_url):
    alembic_cfg = Config(config_uri, 'app:main')
    return alembic_cfg


def main(argv=None):
    command = MigrateCommand(argv or sys.argv[1:])
    return command.run()
