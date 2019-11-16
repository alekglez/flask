# -*- coding: utf-8 -*-

import os
from flask import Flask
from .apps import blueprints
from .extensions import db


def create_app(app_name=__name__, cli=False, testing=False):
    flask_app = Flask(app_name)
    configure_app(flask_app, testing)
    configure_database(flask_app, testing)
    configure_blueprints(flask_app)
    return flask_app


def configure_app(app, testing=False):
    config_env = os.getenv('APP_ENV', 'develop')
    print(f'Using configuration for: {config_env} environment.')
    app.config.from_object(f"project.settings.{config_env}")


def configure_database(app, testing=False):
    if testing:
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('SQLALCHEMY_DATABASE_TEST_URI')

    from .apps.products import models
    db.init_app(app)


def configure_blueprints(app):
    """ Configure blueprints in views. """
    for bp in blueprints:
        app.register_blueprint(bp)
