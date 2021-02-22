import unittest

from app import app, client
from app.models import User, Game

db = client['test']

class TestUser(unittest.TestCase):
    # clear before tests
    try:       
        User.create('alice').delete()
    except Exception:
        User('alice').delete()

    def test_user_create(self):
        user = User.create('alice')
        self.assertEqual(user.username, 'alice')
        user.delete()
 
    def test_user_created_twice(self):
        user = User.create('alice')
        self.assertRaises(Exception, User.create, pk='alice')
        user.delete()

    def test_user_delete_and_access_deleted(self):
        user = User.create('alice')
        user.delete()
        self.assertRaises(Exception, User, pk='alice')

    def test_user_read(self):
        user = User.create('alice')
        self.assertEqual(user, user.read())
        user.delete()

    def test_user_updated_instance(self):
        user = User.create('alice', password='qwerty')
        before = user.password
        user.update(password='123456')   # update invokes read() method
        after = user.password
        self.assertNotEqual(before, after)
        user.delete()

    def test_user_str(self):
        user = User.create('alice')
        self.assertEqual(str(user), '<User:username=alice>')
        user.delete()

class TestGame(unittest.TestCase):
    def test_game_validate_id(self):
        self.assertTrue(Game.validate_id('validid'))
        self.assertTrue(Game.validate_id('valid_ID123'))
        self.assertFalse(Game.validate_id('23invalid'))
        self.assertFalse(Game.validate_id('_somethingFalse'))
        self.assertFalse(Game.validate_id('tooShort'[:3]))
        self.assertFalse(Game.validate_id('tooLong'*10))
        self.assertFalse(Game.validate_id('no spaces allowed'))
        self.assertFalse(Game.validate_id('punctution-not-allowed'))