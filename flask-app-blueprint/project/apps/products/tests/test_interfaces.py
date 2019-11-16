# -*- coding: utf-8 -*-

import json
from apps.core.mixins import CreateApplicationTest


class ProductTestCases(CreateApplicationTest):
    def create_product(self, data=None):
        if not data:
            data = {"name": "Product Example X", "price": 5.0, "supplier": "some-supplier", "category": "IT"}
        return self.client.post('/products/', data=json.dumps(data), content_type='application/json')

    def test_get_all_products(self):
        response = self.client.get('/products/')
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json)

    def test_create_product(self):
        response = self.create_product()
        self.assertEqual(200, response.status_code)

        response = self.client.get('/products/')
        self.assertNotEqual([], response.json)

    def test_create_product_bad_schema(self):
        response = self.client.post('/products/', data=json.dumps({}), content_type='application/json')
        self.assertEqual(400, response.status_code)

        response = self.client.post('/products/', data=json.dumps({'id': 5}), content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_get_products(self):
        self.create_product()
        response = self.client.get('/products/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json[0].get('id', False))

    def test_update_product(self):
        product_name = 'Software Development'
        self.create_product()

        response = self.client.get('/products/')
        self.assertNotEqual([], response.json)
        product_id = response.json[0].get('id')

        response = self.client.put(
            f'/products/{product_id}',
            data=json.dumps({'name': product_name}),
            content_type='application/json')

        self.assertEqual(200, response.status_code)

        response = self.client.get(f'/products/{product_id}')
        self.assertEqual(200, response.status_code)
        self.assertEqual(product_name, response.json.get('name', ''))

    def test_delete_product(self):
        product_id = 1
        self.create_product()

        response = self.client.delete(f'/products/{product_id}')
        self.assertEqual(200, response.status_code)

        response = self.client.get(f'/products/{product_id}')
        self.assertEqual(204, response.status_code)
