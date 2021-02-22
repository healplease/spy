import re

from utils.models import Model


class User(Model):
    collection = 'users'
    pk = 'username'


class Game(Model):
    collection = 'games'
    pk = 'gameId'

    @staticmethod
    def validate_id(game_id: str) -> bool:
        return bool(re.match(r'^[A-Za-z][A-Za-z_0-9]{3,31}$', game_id))