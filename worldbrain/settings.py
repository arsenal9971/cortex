import logging
import os

from configurations import Configuration, values

logger = logging.getLogger(__name__)


class Django:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'worldbrain.cortex',
        'fsm_admin',
        'django_fsm_log',
        'rest_framework',
        'django_extensions',
        'kombu.transport.django',
    ]

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'worldbrain', 'cortex')
            ],
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

    SECRET_KEY = values.SecretValue()

    DEBUG = False

    ROOT_URLCONF = 'worldbrain.urls'

    WSGI_APPLICATION = 'worldbrain.wsgi.application'

    LOGIN_URL = '/admin/'

    DEFAULT_FROM_EMAIl = 'info@worldbrain.io'

    ALLOWED_HOSTS = []

    STATIC_URL = '/static/'

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
            'worldbrain.cortex': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO'
        },
    }

    @property
    def DATABASES(self):
        databases = values.DatabaseURLValue()
        return databases.value


class DjangoRestFramework:
    REST_FRAMEWORK = {}


class Celery:
    BROKER_URL = 'django://'


class BaseSettings(Django, DjangoRestFramework, Celery):
    @classmethod
    def setup(cls):
        super().setup()
        logging.info("settings.ENVIRONMENT: {}".format(cls.ENVIRONMENT))


class FilterThirdPartyDeprecationWarnings:
    @classmethod
    def setup(cls):
        super().setup()

        import worldbrain
        WORLDBRAIN_PATH = os.path.dirname(worldbrain.__file__)

        def filter_deprecation_warnings(record):
            warnings_to_suppress = ['RemovedInDjango110Warning']
            msg = record.getMessage()
            return not any([warn in msg
                            for warn in warnings_to_suppress
                            if not msg.startswith(WORLDBRAIN_PATH)])
        logging.getLogger('py.warnings').addFilter(filter_deprecation_warnings)


class Development(FilterThirdPartyDeprecationWarnings,
                  BaseSettings, Configuration):
    DEBUG = True

    MEDIA_ROOT = '/tmp/images'

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

    CORS_ORIGIN_ALLOW_ALL = True

    ENVIRONMENT = 'development'


class Testing(BaseSettings, Configuration):
    ENVIRONMENT = 'testing'


class Production(BaseSettings, Configuration):
    ENVIRONMENT = 'production'


class Travis(BaseSettings, Configuration):
    ENVIRONMENT = 'travis'
