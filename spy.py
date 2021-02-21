from socket import gethostbyname, gethostname
import unittest

from app import app

if __name__ == '__main__':
    if app.config.get('TESTING'):
        unittest.main(module='app.tests', )

    app.run(gethostbyname(gethostname()), port=3030)