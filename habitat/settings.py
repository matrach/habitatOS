import os
from django.conf.locale.en import formats as en_formats
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_URLCONF = 'habitat.urls'
WSGI_APPLICATION = 'habitat.wsgi.application'

# Development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '57aq0)wd*_kz&9r1#3rpw@+%n326zlrt+c3pr=&dgfa^^@d_ix'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'habitatos.space',
    'test.habitatos.space',
    'lunex1.habitatos.space',
    'icares1.habitatos.space',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS = [
    'grappelli.dashboard',
    'grappelli',
    'import_export',
    'rest_framework',
    'rest_framework_swagger',
    'devutils',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'habitat._common',
    'habitat.biolab',
    'habitat.building',
    'habitat.communication',
    'habitat.dashboard',
    'habitat.extravehicular',
    'habitat.food',
    'habitat.health',
    'habitat.inventory',
    'habitat.reporting',
    'habitat.sensors',
    'habitat.timezone',
    'habitat.water',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tmp', 'HabitatOS-database.sqlite3'),
    }
}

if os.environ.get('DATABASE_URL'):
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()


# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

en_formats.DATETIME_FORMAT = 'Y-m-d H:i'
en_formats.DATE_FORMAT = 'Y-m-d'
en_formats.TIME_FORMAT = 'H:i'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')


admin.site.site_header = _('HabitatOS')
admin.site.index_title = _('Dashboard')
admin.site.site_title = _('HabitatOS')

GRAPPELLI_ADMIN_TITLE = _('HabitatOS')
GRAPPELLI_INDEX_DASHBOARD = 'habitat.dashboard.icares1.AdminDashboard'
GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
    'auth': {
        'user': ['username__icontains']
    }
}

if os.path.exists('/tmp/memcached.sock'):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
            'LOCATION': '/tmp/memcached.sock',

            # Use binary memcache protocol (needed for authentication)
            'BINARY': True,

            # TIMEOUT is not the connection timeout! It's the default expiration
            # timeout that should be applied to keys! Setting it to `None`
            # disables expiration.
            'TIMEOUT': None,

            'OPTIONS': {
                # Enable faster IO
                'tcp_nodelay': True,

                # Keep connection alive
                'tcp_keepalive': True,

                # Timeout settings
                'connect_timeout': 2000,  # ms
                'send_timeout': 750*1000,  # us
                'receive_timeout': 750*1000,  # us
                '_poll_timeout': 2000,  # ms

                # Better failover
                'ketama': True,
                'remove_failed': 1,
                'retry_timeout': 2,
                'dead_timeout': 30,
            }
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
        }
    }

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'list',
    'OPERATIONS_SORTER': 'alpha',
    'api_version': '1.0',
}

HABITATOS = {
    'TIME_ZONE': 'habitat.timezone.MartianStandardTime',
}
