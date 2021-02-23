from app import app, db, client

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
            raise Exception(f'Instance with this {self.__class__.pk} not found.')

        self.instance = instance

    def __str__(self):
        return f'<{self.__class__.__name__}:{self.__class__.pk}={self.instance[self.pk]}>'

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
        query = { self.__class__.pk: self.instance[self.__class__.pk] }
        instance = db[self.__class__.collection].find_one(query, ID_PROJECTION)
        self.instance = instance
        return self # not sure is need to return it, but why not

    def update(self, *args, **kwargs):
        kwargs.pop(self.__class__.pk, None) # prevent updating of the pk itself - it can't be changed through model

        if kwargs:  # if we have what to update :D
            query = { self.__class__.pk: self.instance[self.__class__.pk] }
            update = { '$set': kwargs }
            db[self.__class__.collection].update_one(query, update)
        
        self.read()  # update the instance as well

    def delete(self):
        query = { self.__class__.pk: self.instance[self.__class__.pk] }
        db[self.__class__.collection].delete_one(query)

        # TODO: display deletion result