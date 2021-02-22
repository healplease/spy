import unittest

from app import app, client
from app.models import User, Game

db = client['test']

class TestUser(unittest.TestCase):
    def test_user_create(self):
        user = User.create('alice')
        self.assertEqual(user.username, 'alice')
        user.delete()

    def test_user_delete(self):
        user = User.create('alice')
        user.delete()
        self.assertRaises(Exception, User, pk='alice')

    def test_user_str(self):
        user = User.create('alice')
        self.assertEqual(str(user), '<User:username=alice>')
        user.delete()
