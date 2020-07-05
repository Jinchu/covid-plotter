import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Secret-Youll-Never-Guess'

STATIC_CONT = 'https://www.example.com/plots/'

