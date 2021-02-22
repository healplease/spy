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

    def test_game_validate_id(self):
        self.assertTrue(Game.validate_id('validid'))
        self.assertTrue(Game.validate_id('valid_ID123'))
        self.assertFalse(Game.validate_id('23invalid'))
        self.assertFalse(Game.validate_id('_somethingFalse'))
        self.assertFalse(Game.validate_id('tooShort'[:3]))
        self.assertFalse(Game.validate_id('tooLong'*10))
        self.assertFalse(Game.validate_id('no spaces allowed'))
        self.assertFalse(Game.validate_id('punctution-not-allowed'))