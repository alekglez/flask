# -*- coding: utf-8 -*-

from ..mixins import CreateApplicationTest


class CoreTestCases(CreateApplicationTest):
    def test_get_all_products(self):
        response = self.client.get('/health/')
        self.assertEqual(200, response.status_code)
        self.assertTrue(isinstance(response.json.get('database', False), dict))
