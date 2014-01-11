# Django settings for caravan project.
import os
import sys

from caravan import exceptions

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'data.db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

SITE_BRANDING = 'Caravan Dashboard'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
BIN_DIR = os.path.abspath(os.path.join(ROOT_PATH, '..', 'bin'))

if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(ROOT_PATH, '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(ROOT_PATH, '..', 'static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(
            ROOT_PATH, 'static')),
    os.path.abspath(os.path.join(
            ROOT_PATH, '..', 'openstack_dashboard/static')),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = None

if not SECRET_KEY:
    from horizon.utils import secret_key
    LOCAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    SECRET_KEY = secret_key.generate_or_read_from_file(os.path.join(LOCAL_PATH,
                                                       '.secret_key_store'))

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
    'horizon.loaders.TemplateLoader'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'horizon.middleware.HorizonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'caravan.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'caravan.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
    os.path.join(ROOT_PATH, '../openstack_dashboard/templates'),
    os.path.join(ROOT_PATH, '../horizon/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'horizon.context_processors.horizon',
#    'openstack_dashboard.context_processors.openstack',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.humanize',
    'compressor',
    'horizon',
    'caravan.dashboards.tasks',
    'caravan.dashboards.infrastructure',
    'caravan.dashboards.results',
)

#SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


HORIZON_CONFIG = {
    'dashboards': ('tasks', 'infrastructure', 'results'),
#    'user_home': 'caravan.dashboards.tasks',
    'ajax_queue_limit': 10,
    'auto_fade_alerts': {
        'delay': 3000,
        'fade_duration': 1500,
        'types': ['alert-success', 'alert-info']
    },
#    'help_url': "http://example.com",
    'exceptions': {'recoverable': exceptions.RECOVERABLE,
                   'not_found': exceptions.NOT_FOUND,
                   'unauthorized': exceptions.UNAUTHORIZED},
}

LOGIN_URL = '/auth/login/'
LOGOUT_URL = '/auth/logout/'
# LOGIN_REDIRECT_URL can be used as an alternative for
# HORIZON_CONFIG.user_home, if user_home is not set.
# Do not set it to '/home/', as this will cause circular redirect loop
LOGIN_REDIRECT_URL = '/'


STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/less', ('lesscpy {infile}')),
)

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
)

COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'dashboard'
COMPRESS_CSS_HASHING_METHOD = 'hash'
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
COMPRESS_OFFLINE = True

DEFAULT_EXCEPTION_REPORTER_FILTER = 'horizon.exceptions.HorizonReporterFilter'

# Add HORIZON_CONFIG to the context information for offline compression
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'HORIZON_CONFIG': HORIZON_CONFIG
}


LANGUAGE_CODE = 'en'
LANGUAGE_COOKIE_NAME = 'horizon_language'
USE_I18N = True
USE_L10N = True
USE_TZ = True
