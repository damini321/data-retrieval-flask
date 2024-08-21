import unittest
from app import create_app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_fetch_data(self):
        response = self.client.get('/fetch-data')
        self.assertEqual(response.status_code, 200)

    def test_get_processed_data(self):
        self.client.get('/fetch-data')
        response = self.client.get('/get-processed-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn("sum", response.get_json())

if __name__ == '__main__':
    unittest.main()
