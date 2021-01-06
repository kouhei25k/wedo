import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '^^d=6fu+&^flz65bg#@g8bzb$rx882(8&8ev3e*r@gk^v+t^)4'

from database import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': name,
        'USER': user,
        'PASSWORD':password,
        'HOST': '127.0.0.1',
        'POST': '5432',

    }
}