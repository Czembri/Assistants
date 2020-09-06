import unittest
from app.handlers import app, db

class TestApp(unittest.TestCase):
    def setup(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_root(self):
        resposne = self.app.get('/', follow_redirects=True)
        self.assertEqual(resposne.status_code, 200)

if __name__ == '__main__':
    unittest.main()