# -*- coding: utf-8 -*-
'''
Production Configurations
- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use sendgrid to send emails
- Use MEMCACHIER on Heroku
'''

import os

from .common import *  # noqa

# Also read .env file

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECRET KEY
SECRET_KEY = env("DJANGO_SECRET_KEY")
# END SECRET KEY

# django-secure
INSTALLED_APPS += ('djangosecure', 'gunicorn', 'storages',)

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_FRAME_DENY = env.bool("DJANGO_SECURE_FRAME_DENY", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=False)
SESSION_COOKIE_HTTPONLY = env.bool("DJANGO_SESSION_COOKIE_HTTPONLY", default=True)
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
# end django-secure

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])
# END SITE CONFIGURATION

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env.str('DJANGO_AWS_S3_REGION_NAME', 'us-east-1')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = env.bool("DJANGO_AWS_QUERYSTRING_AUTH", default=False)

# see: https://github.com/antonagestam/collectfast
AWS_PRELOAD_METADATA = True

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (
        AWS_EXPIRY, AWS_EXPIRY)
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
# END STORAGE CONFIGURATION


# EMAIL
EMAIL_HOST = env.str('EMAIL_HOST', 'smtp.sendgrid.com')
EMAIL_HOST_PASSWORD = env('SENDGRID_PASSWORD')
EMAIL_HOST_USER = env('SENDGRID_USERNAME')
EMAIL_PORT = env.int('EMAIL_PORT', 587)
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': os.environ.get('MEMCACHIER_SERVERS'),
        'OPTIONS': {
            'username': os.environ.get('MEMCACHIER_USERNAME'),
            'password': os.environ.get('MEMCACHIER_PASSWORD')
        }
    }
}
