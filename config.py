import os
from random import randint

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET KEY' # Prevents CSRF attacks
    SEND_FILE_MAX_AGE_DEFAULT = 0                                                                     
    PORT = 8787                                               # port to run server on                                                            # IP adress + port to display on qr
    ROOT = os.path.dirname(os.path.abspath(__file__))
    