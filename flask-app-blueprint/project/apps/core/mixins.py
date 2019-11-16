# -*- coding: utf-8 -*-

from unittest import TestCase
from project.app import create_app
from project.extensions import db


class CreateApplicationTest(TestCase):
    def setUp(self) -> None:
        self.app = create_app(app_name='project-test-execution', cli=True, testing=True)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self) -> None:
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
