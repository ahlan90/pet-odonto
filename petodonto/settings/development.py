from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i*xs-kr1fv7vtf7cc=d7a)+wh*ldowr^&_zb1y&@*^6+7d@^mc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}