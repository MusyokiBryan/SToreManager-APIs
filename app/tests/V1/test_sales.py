import unittest
import sys  # fix import errors
import os
from app.tests.V1.base import ConfigTestCase
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class SalesTest(ConfigTestCase):
    """this class contains Product tests"""

    def test_see_sales(self):
        response = self.client().get()
        self.assertEqual(response.status_code, 200)

    def test_get_a_sale(self):
        response = self.client().get()
        self.assertEqual(response.status_code, 200)

    def test_post_a_sale(self):
        response = self.client().post(data=json.dumps(sale),
                                      content_type="application/json")
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
