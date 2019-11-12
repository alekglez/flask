# -*- coding: utf-8 -*-

from flask import Flask
from .apps import blueprints


def create_app(app_name=__name__, cli=False, testing=False):
    flask_app = Flask(app_name)
    configure_app(flask_app, testing)
    configure_blueprints(flask_app)
    return flask_app


def configure_app(app, testing=False):
    pass


def configure_blueprints(app):
    """ Configure blueprints in views. """
    for bp in blueprints:
        app.register_blueprint(bp)
