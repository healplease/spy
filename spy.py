from socket import gethostbyname, gethostname
import unittest

from app import app

if __name__ == '__main__':
    app.run(
        host=app.config['FLASK_HOST'], 
        port=app.config['FLASK_PORT'],
    )