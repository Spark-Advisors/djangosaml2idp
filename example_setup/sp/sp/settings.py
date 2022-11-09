"""
Django settings for sp project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ar249h_c(@5#x)ha_vou=4%plz*#!*l=+4c^jbo6wi%8z222hg"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djangosaml2",
    "sp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sp.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "sp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"

# Everything above are default settings made by django-admin startproject
# The following is added for djangosaml2 SP configuration.
# See their docs for explanation of all options.

import saml2  # noqa
from saml2.saml import NAMEID_FORMAT_EMAILADDRESS  # noqa
from saml2.sigver import get_xmlsec_binary  # noqa

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "djangosaml2.backends.Saml2Backend",
)

APPEND_SLASH = False
LOGIN_URL = "/saml2/login/"
LOGOUT_URL = "/logout/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SAML_CONFIG = {
    "debug": DEBUG,
    "xmlsec_binary": get_xmlsec_binary(["/opt/local/bin", "/usr/bin/xmlsec1"]),
    "entityid": "http://localhost:8000/saml2/metadata/",
    "service": {
        "sp": {
            "name": "http://localhost:8000/saml2/metadata/",
            "endpoints": {
                "assertion_consumer_service": [
                    ("http://localhost:8000/saml2/acs/", saml2.BINDING_HTTP_POST),
                ],
                "single_logout_service": [
                    ("http://localhost:8000/saml2/ls/", saml2.BINDING_HTTP_REDIRECT),
                    ("http://localhost:8000/saml2/ls/post/", saml2.BINDING_HTTP_POST),
                ],
            },
            "name_id_format": [NAMEID_FORMAT_EMAILADDRESS],
            "authn_requests_signed": True,
            "want_response_signed": True,
            "want_assertions_signed": True,
            "allow_unsolicited": True,
        },
    },
    "attribute_map_dir": os.path.join(
        os.path.join(os.path.join(BASE_DIR, "sp"), "saml2_config"), "attribute-maps"
    ),
    "metadata": {
        "local": [
            os.path.join(
                os.path.join(os.path.join(BASE_DIR, "sp"), "saml2_config"),
                "idp_metadata.xml",
            )
        ],
    },
    # Signing
    "key_file": BASE_DIR + "/certificates/private.key",
    "cert_file": BASE_DIR + "/certificates/public.cert",
    # Encryption
    "encryption_keypairs": [
        {
            "key_file": BASE_DIR + "/certificates/private.key",
            "cert_file": BASE_DIR + "/certificates/public.cert",
        }
    ],
    "valid_for": 365 * 24,
}

SAML_USE_NAME_ID_AS_USERNAME = True
SAML_DJANGO_USER_MAIN_ATTRIBUTE = "username"
SAML_DJANGO_USER_MAIN_ATTRIBUTE_LOOKUP = "__iexact"
SAML_CREATE_UNKNOWN_USER = True

SAML_ATTRIBUTE_MAPPING = {
    # SAML: DJANGO
    # Must also be present in attribute-maps!
    "email": ("email",),
    "first_name": ("first_name",),
    "last_name": ("last_name",),
    "is_staff": ("is_staff",),
    "is_superuser": ("is_superuser",),
}
