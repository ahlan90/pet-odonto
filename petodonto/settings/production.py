from .base import *
from decouple import config
import dj_database_url

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=True, cast=bool)

DATABASES = {
    'default': dj_database_url.config(
        default=config('HEROKU_POSTGRESQL_PINK_URL')
    )
}