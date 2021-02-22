import os
from urllib import parse

class Config():
    # main settings
    DEBUG = bool(os.environ.get('FLASK_DEBUG', 1))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask')

    TESTING = True

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