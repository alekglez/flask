# -*- coding: utf-8 -*-

from ..models import Product
from apps.core.mixins import CreateApplicationTest
from project.extensions import db


class TestProductModel(CreateApplicationTest):
    def test_model_product(self):
        product = Product(name='ProductX', category='IT', supplier='CompanyX', price=500.0)
        db.session.add(product)
        self.assertEqual(Product.query.filter_by(name=product.name).first().name, product.name)
