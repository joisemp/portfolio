from . base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR, 'static']

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'