import re

from utils.models import Model


class User(Model):
    collection = 'users'
    pk = 'username'

    @staticmethod
    def validate_id(username: str) -> bool:
        return bool(re.match(r'^[A-Za-z][A-Za-z_0-9]{3,31}$', username))

    @classmethod
    def create(cls, pk:str, *args, **kwargs):
        if cls.validate_id(pk):
            return super(User, cls).create(pk, *args, **kwargs)
        else:
            raise Exception(f'Validation error: {cls.pk} must be an indentifier')


class Game(Model):
    collection = 'games'
    pk = 'gameId'

    @staticmethod
    def validate_id(game_id: str) -> bool:
        return bool(re.match(r'^[A-Za-z][A-Za-z_0-9]{3,31}$', game_id))

    @classmethod
    def create(cls, pk:str, *args, **kwargs):
        if cls.validate_id(pk):
            return super(Game, cls).create(pk, *args, **kwargs)
        else:
            raise Exception(f'Validation error: {cls.pk} must be an indentifier')