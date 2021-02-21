import re

from app import app, db, client

ID_PROJECTION = { '_id': 0 }


class Model:
    collection = 'test'
    pk = '_id'

    def __init__(self, pk: str='', *args, **kwargs):
        if not db[self.collection]:
            raise Exception(f'Collection {self.collection} not found')

        self.instance = {}
        
        if pk:
            query = { self.pk: pk }
            instance = db[self.collection].find_one(query, ID_PROJECTION)
            self.instance = instance

    def get(self):
        return self.instance


class User(Model):
    table = 'users'
    id_field = 'username'

    def get_id(self):
        return self.instance['username']


class Game(Model):
    id_field = 'gameId'

    def __init__(self, game_id: str='', *args, **kwargs):
        self.instance = {}

        if game_id:
            query = { 'gameId': game_id }
            game = db.games.find_one(query, ID_PROJECTION)

            if game:
                self.instance = game

    @staticmethod
    def validate_id(game_id: str) -> bool:
        return bool(re.match(r'[A-Za-z][A-Za-z_0-9]{3,31}', game_id))
        # return game_id.isidentifier() and (4 <= game_id <= 32)

    @classmethod
    def create(cls, game_id: str=None, *args, **kwargs):
        pass