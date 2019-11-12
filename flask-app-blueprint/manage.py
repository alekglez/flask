# -*- coding: utf-8 -*-

import sys
import click
from flask.cli import FlaskGroup

from project.app import create_app


def run():
    return create_app(cli=True, testing=True if sys.argv[1] == 'test' else False)


@click.group(cls=FlaskGroup, create_app=run)
def run_server():
    """ App main entry point """
    pass


if __name__ == '__main__':
    run_server()
