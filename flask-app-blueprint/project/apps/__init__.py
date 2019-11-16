# -*- coding: utf-8 -*-

from .core.interfaces import core
from .frontend.views import frontend
from .products.interfaces import products


blueprints = [core, frontend, products]
