# -*- coding: utf-8 -*-

from project.extensions import db


def database_status():
    """
    Verify database status.
    :return: Return {status: ..., description: ...}
    """

    try:
        db.session.execute('SELECT 1;')
        return dict(status='green', description='Database up and running!')

    except Exception as error:
        return dict(status='red', description=str(error))
