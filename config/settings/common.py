# -*- coding: utf-8 -*-
"""
Django settings for project.
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

import environ

BASE_DIR = environ.Path(__file__) - 3  # (/a/myfile.py - 2 = /)
CONFIG_DIR = BASE_DIR.path('config')

env = environ.Env()

# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'jet',
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'rest_framework',  # REST Framework
    'rest_framework.authtoken',
    'corsheaders',
    'smart_selects',
    'tinymce',
    'import_export',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'jurisdiction',
    'survey',
    'mailman',
    'pages'
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# END MIDDLEWARE CONFIGURATION

# DEBUG
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
#       In production, this is changed to a values.SecretValue() setting
SECRET_KEY = 'CHANGEME!!!'
# END SECRET CONFIGURATION

# FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS

FIXTURE_DIRS = (
    str(CONFIG_DIR.path('fixtures')),
)


# END FIXTURE CONFIGURATION

# EMAIL CONFIGURATION
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
# END EMAIL CONFIGURATION

# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMIN_EMAIL = env('ADMIN_EMAIL', default='info@fairelectionscenter.org')

ADMINS = (
    ("""DevOps""", ADMIN_EMAIL),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION

# Contact us email
CONTACT_US = env('CONTACT_US', default='info@fairelectionscenter.org')
DEFAULT_FROM_EMAIL = env(
    'DEFAULT_FROM_EMAIL', default='info@fairelectionscenter.org')
DEFAULT_SURVEY_FROM_EMAIL = env(
    'DEFAULT_SURVEY_FROM_EMAIL', default=DEFAULT_FROM_EMAIL)
TEST_TO_EMAIL = env('TEST_TO_EMAIL', default=None)

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db("DATABASE_URL", default='sqlite:///%s' % str(CONFIG_DIR.path('db.sqlite3'))),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# END DATABASE CONFIGURATION

# CACHING
# Do this here because thanks to django-pylibmc-sasl and pylibmc
# memcacheify (used on heroku) is painful to install on windows.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'OPTIONS': {
            'MAX_ENTRIES': 20000
        }
    }
}
# END CACHING

# GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/New_York'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = env.int('DJANGO_SITE_ID', 1)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# END GENERAL CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': False,
    'DIRS': [
        str(BASE_DIR.path('config/templates')),
    ],
    'OPTIONS': {
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
        'debug': DEBUG,
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
    },
}]

# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(CONFIG_DIR.path('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(CONFIG_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# END STATIC FILE CONFIGURATION

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(CONFIG_DIR.path('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION

# URL Configuration
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'
# End URL Configuration

# AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Session management
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
USE_X_FORWARDED_HOST = env.bool('DJANGO_USE_X_FORWARDED_HOST', True)


# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# END LOGGING CONFIGURATION

# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 51
}
# END REST FRAMEWORK CONFIGURATION


# Django CORS
CORS_ORIGIN_ALLOW_ALL = env.bool('DJANGO_CORS_ORIGIN_ALLOW_ALL', True)
CORS_ALLOW_CREDENTIALS = env.bool('DJANGO_CORS_ALLOW_CREDENTIALS', True)
# End Django CORS

# TINY MCE
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'width': 600,
    'height': 500,
}
# END TINY MCE

JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
    {'label': 'Jurisdictions', 'app_label': 'jurisdiction', 'items': [
        {'name': 'jurisdiction.state'},
        {'name': 'jurisdiction.jurisdiction'},
        {'name': 'jurisdiction.surveyemail'},
    ]},
    {'label': 'Pages', 'app_label': 'pages', 'items': [
        {'name': 'pages.page'},
    ]},
    {'label': 'Surveys', 'app_label': 'survey', 'items': [
        {'name': 'survey.survey'},
        {'name': 'survey.application'},
    ]},
]

SITE_TITLE = env.str('SITE_TITLE', 'FEC')
SITE_HEADER = env.str('SITE_HEADER', 'Work Elections')
SITE_URL = env.str('SITE_URL', 'https://workelections.com')
JQUERY_URL = False


SURVEY_MONKEY_URL = env.str('SURVEY_MONKEY_URL', 'http://example.com') + '{}'
WORKELECTION_WEBHOOK_USERNAME = env.str('WORKELECTION_WEBHOOK_USERNAME', 'testusername')
WORKELECTION_WEBHOOK_PASSWORD = env.str('WORKELECTION_WEBHOOK_PASSWORD', 'testpassword')
