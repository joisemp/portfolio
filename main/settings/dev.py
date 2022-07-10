from . base import *

SECRET_KEY = 'django-insecure-iuj=-rae8+6d4mo9@df%29=+tsnyw7kuy-hc027tut8$ckq+p!'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'