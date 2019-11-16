# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify
from .utils import database_status

core = Blueprint('core', __name__, url_prefix='/')


@core.route('/health/', methods=['GET'])
def health(**kwargs):
    return jsonify({
        'database': database_status()
    })
