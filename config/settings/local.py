# -*- coding: utf-8 -*-
'''
Local Configurations
- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
'''

# read .env file first
import environ
BASE_DIR = environ.Path(__file__) - 3  # (/a/myfile.py - 2 = /)
CONFIG_DIR = BASE_DIR.path('config')
env = environ.Env()
environ.Env.read_env(str(CONFIG_DIR.path('env/.local')))

from .common import *  # noqa
"""
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
"""
# EMAIL
EMAIL_HOST = env.str('EMAIL_HOST', 'smtp.sendgrid.com')
EMAIL_HOST_PASSWORD = env('SENDGRID_PASSWORD')
EMAIL_HOST_USER = env('SENDGRID_USERNAME')
EMAIL_PORT = env.int('EMAIL_PORT', 587)
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

EMAIL_BACKEND = env('EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

# DEBUG
DEBUG = env.bool('DJANGO_DEBUG', default=True)
# END DEBUG

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

# Your local stuff: Below this line define 3rd party library settings
SURVEY_URL = env('SURVEYURL') + '{}'
USERNAME = env('USERNAME')
PASSWORD = env('PASSWORD')