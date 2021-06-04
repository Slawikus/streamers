import os
from pathlib import Path
import dj_database_url
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG_MODE") == "True"

# TODO: Change this later to allow only specific hosts
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'channels',
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_extensions",
    # 3rd party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "crispy_forms",
    "django_filters",
    "bootstrap4",
    "bootstrap_datepicker_plus",
    "ckeditor",
    "mapbox_location_field",
    "phonenumber_field",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "dal",
    "dal_select2",
    # Local
    "accounts",
    "events",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "configuration.middleware.MoveJWTCookieIntoTheBody",
    # "configuration.middleware.MoveJWTRefreshCookieIntoTheBody",
]

ROOT_URLCONF = "configuration.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            'string_if_invalid': 'INVALID EXPRESSION: %s',
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "configuration.wsgi.application"
ASGI_APPLICATION = 'configuration.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {"default": dj_database_url.config()}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"


TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

LANGUAGES = [
    ("en", "English"),
    ("ru", "Russian"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Email-related setup
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
CRISPY_TEMPLATE_PACK = "bootstrap4"

MAPBOX_KEY = os.environ.get("MAPBOX_KEY")

# Authentication

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": "rest_framework.permissions.IsAuthenticated",
}

REST_SESSION_LOGIN = False
REST_USE_JWT = True
JWT_AUTH_COOKIE = "my-app-auth"
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"
JWT_AUTH_SECURE = True
CORS_ALLOW_CREDENTIALS = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

AUTH_USER_MODEL = "accounts.CustomUser"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

if SENDGRID_API_KEY:
    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    "social_core.backends.facebook.FacebookOAuth2",
)

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_FORMS = {
    "signup": "accounts.forms.CustomUserCreationForm",
}

LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"


# ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'

SOCIALACCOUNT_PROVIDERS = {
    'facebook':
        {
         'METHOD': 'oauth2',
         'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
         'SCOPE': ['email', 'public_profile'],
         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
         'INIT_PARAMS': {'cookie': True},
         'FIELDS': [
             'id',
             'first_name',
             'last_name',
             'name',
             'name_format',
             'picture',
             'short_name'
         ],
         'EXCHANGE_TOKEN': True,
         'LOCALE_FUNC': lambda request: 'ru_RU',
         'VERIFIED_EMAIL': False,
         'VERSION': 'v7.0',
         # you should fill in 'APP' only if you don't create a Facebook instance at /admin/socialaccount/socialapp/
         'APP': {
             'client_id': '',  # !!! THIS App ID
             'secret': '',  # !!! THIS App Secret
             'key': ''
                }
         }
}

CKEDITOR_CONFIGS = {
    'default': {
        'height': 240,
        'width': '100%'
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
