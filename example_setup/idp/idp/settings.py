"""
Django settings for idp project.

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
SECRET_KEY = "w1#&b@*haty+1pmlw--ll9i!5z+d$e*5yxq0&cgo16e_vhd7r("

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
    "djangosaml2idp",
    "idp",
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

ROOT_URLCONF = "idp.urls"

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

WSGI_APPLICATION = "idp.wsgi.application"


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

STATICFILES_DIRS = (BASE_DIR + "/static/",)


# pySAML2 IDP
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 60  # an hour

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "djangosaml2idp": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}


# Everything above are default settings made by django-admin startproject
# The following is added for djangosaml2idp IdP configuration.

import saml2  # noqa
from saml2.saml import NAMEID_FORMAT_EMAILADDRESS, NAMEID_FORMAT_UNSPECIFIED  # noqa
from saml2.sigver import get_xmlsec_binary  # noqa

APPEND_SLASH = False
LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SAML_IDP_CONFIG = {
    "debug": DEBUG,
    "xmlsec_binary": get_xmlsec_binary(["/opt/local/bin", "/usr/bin/xmlsec1"]),
    "entityid": "http://localhost:9000/idp/metadata/",
    "description": "Example IdP setup",
    "service": {
        "idp": {
            "name": "Django localhost IdP",
            "endpoints": {
                "single_sign_on_service": [
                    ("http://localhost:9000/idp/sso/post/", saml2.BINDING_HTTP_POST),
                    (
                        "http://localhost:9000/idp/sso/redirect/",
                        saml2.BINDING_HTTP_REDIRECT,
                    ),
                ],
                "single_logout_service": [
                    ("http://localhost:9000/idp/slo/post/", saml2.BINDING_HTTP_POST),
                    (
                        "http://localhost:9000/idp/slo/redirect/",
                        saml2.BINDING_HTTP_REDIRECT,
                    ),
                ],
            },
            "name_id_format": [NAMEID_FORMAT_EMAILADDRESS, NAMEID_FORMAT_UNSPECIFIED],
            "sign_response": True,
            "sign_assertion": True,
            "want_authn_requests_signed": True,
        },
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


SAML_AUTHN_SIGN_ALG = saml2.xmldsig.SIG_RSA_SHA256
SAML_AUTHN_DIGEST_ALG = saml2.xmldsig.DIGEST_SHA256
