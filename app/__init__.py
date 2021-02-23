# built-in modules
import os
import unittest

# third-party modules
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

# first-party modules
import config


app = Flask(__name__)
cors = CORS(app)
app.config.from_object(config.Config)

client = MongoClient(app.config.get('DATABASE_URL'))
db = client[app.config.get('MONGO_DATABASE')]


if app.config.get('TESTING'):
    unittest.main(module='app.tests', exit=False)

# import views after app init to escape circular import
from app import views, models, api