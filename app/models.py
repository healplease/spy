import re

from app import app, db, client

db = client['test']
ID_PROJECTION = { '_id': 0 }

class Model(object):
    collection = '_model'
    pk = '_id'

    def __init__(self, pk:str, *args, **kwargs):
        if not db[self.collection]:
            raise Exception(f'Collection {self.collection} not found')
        
        query = { self.pk: pk }
        instance = db[self.collection].find_one(query, ID_PROJECTION)

        if not instance:
            raise Exception('Instance with this PK not found.')

        self.instance = instance

    def __str__(self):
        return f'<{self.__class__.__name__}:{self.pk}={self.instance[self.pk]}>'

    def __getattr__(self, name):
        instance_attrs = [] if not isinstance(self.instance, dict) else list(self.instance.keys())
        if name in instance_attrs:
            return self.instance[name]
        return getattr(self, name)

    @classmethod
    def create(cls, pk:str, *args, **kwargs):

        query = { cls.pk: pk }
        instance = db[cls.collection].find_one(query, ID_PROJECTION)

        if instance:
            raise Exception(f'There is already instance with {cls.pk}={pk}')

        document = {**kwargs, **{ cls.pk: pk }}
        db[cls.collection].insert_one(document)

        return cls(pk)
    
    def read(self):
        return self.instance

    def update(self, *args, **kwargs):
        pass

    def delete(self):
        query = { self.__class__.pk: self.username }
        db[self.__class__.collection].delete_one(query)
        # TODO: display deletion result


class User(Model):
    collection = 'users'
    pk = 'username'


class Game(Model):
    collection = 'games'
    pk = 'gameId'

    @staticmethod
    def validate_id(game_id: str) -> bool:
        return bool(re.match(r'[A-Za-z_][A-Za-z_0-9]{3,31}', game_id))