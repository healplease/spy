import unittest

from app import app, client, models

db = client['test']

class TestUser(unittest.TestCase):
    def test_model(self):
        user = models.User()
        self.assertEqual(user.instance.get('username'), None)
