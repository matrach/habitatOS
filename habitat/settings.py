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
    'habitatos.herokuapp.com',
    'habitatos.space',
    'www.habitatos.space',
    'os.astrotech.io',
    'test.habitatos.space',
]

INSTALLED_APPS = [
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'habitat._common',
    'habitat.dashboard',
    'habitat.biolab',
    'habitat.building',
    'habitat.communication',
    'habitat.food',
    'habitat.health',
    'habitat.inventory',
    'habitat.reporting',
    'habitat.sensors',
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
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
en_formats.DATETIME_FORMAT = 'Y-m-d H:i:s.u'
DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S.%f']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')

FILEBROWSER_VERSIONS_BASEDIR = '_thumbnails'
FILEBROWSER_DIRECTORY = '_uploads/'
FILEBROWSER_STORAGE_LOCATION = '_media'
FILEBROWSER_MAX_UPLOAD_SIZE = 10_737_418_240  # 10 GB
FILEBROWSER_NORMALIZE_FILENAME = True
FILEBROWSER_CONVERT_FILENAME = True

FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', '.docx', '.xslx', '.pptx', '.odt', '.odx'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', 'mp4'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
}

FILEBROWSER_SELECT_FORMATS = {
    'file': ['Image', 'Document', 'Video', 'Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
}

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
}

admin.site.site_header = _('HabitatOS')
admin.site.index_title = _('Dashboard')
admin.site.site_title = _('HabitatOS')

GRAPPELLI_ADMIN_TITLE = _('HabitatOS')
GRAPPELLI_INDEX_DASHBOARD = 'habitat.dashboard.IndexDashboard'

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
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
        }
    }
