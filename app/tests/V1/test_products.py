import unittest
import sys  # fix import errors
import os
from app.tests.V1.base import ConfigTestCase
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ProductTest(ConfigTestCase):
    """this class contains Product tests"""

    def test_get_products(self):
        response = self.client().get("/api/v1/products")
        self.assertEqual(response.status_code, 200)

    def test_get_a_product(self):
        response = self.client().get("/api/v1/product/1")
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        product = {"product_name": "shirts", "product_price": 5500}
        response = self.client().post("/api/v1/products", data=json.dumps(product), content_type="application/json")
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
