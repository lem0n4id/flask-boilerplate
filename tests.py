import unittest
from app import app

class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)

    # ensure that flask was set up correctly
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # ensure that the site loads up correctly
    def test_home_page(self):
        response = self.client.get('/', content_type='html/text')
        self.assertTrue(b"Hello World!" in response.data)
        
if __name__ == "__main__":
    unittest.main()