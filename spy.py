from socket import gethostbyname, gethostname

from app import app

if __name__ == '__main__':
    app.run(gethostbyname(gethostname()), port=3030)