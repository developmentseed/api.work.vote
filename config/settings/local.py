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
environ.Env.read_env(str(CONFIG_DIR.path('env/.local')))

from .common import *  # noqa

# DEBUG
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATE_DEBUG = DEBUG
# END DEBUG

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

# Your local stuff: Below this line define 3rd party library settings
