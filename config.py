import os
from urllib import parse

class Config():
    DEBUG = os.environ.get('FLASK_DEBUG', True)
    SECRET_KEY = 'testkey'

    # main settings
    DEBUG = True
    SECRET_KEY = 'flask'

    # database settings
    MONGO_PROTOCOL = 'mongodb+srv'
    MONGO_USER = 'healplease'
    MONGO_PASSWORD = 'Alex2020'
    MONGO_HOST = 'dimabot.tfomu.mongodb.net'
    MONGO_DATABASE = 'spy'
    MONGO_ARGUMENTS = {
        'retryWrites': 'true',
        'w': 'majority'
    }

    DATABASE_URL = f'{MONGO_PROTOCOL}://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONGO_DATABASE}{"?" if MONGO_ARGUMENTS else ""}{parse.urlencode(tuple(MONGO_ARGUMENTS.items()))}'