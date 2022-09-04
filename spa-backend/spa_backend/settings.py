"""
Django settings for spa_backend project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import enum
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!!!x2on6t7z575w(_d9=fqhuek7ig=68pla7&vkyz8rni%!ch@"

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
    # Third Party
    "rest_framework",
    "corsheaders",
    # First Party
    "accounts",
    "reminders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "spa_backend.urls"

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

WSGI_APPLICATION = "spa_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST FRAMEWORK
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}


# ------------------------------------------------ CSRF SCENARIOS --------------------------------------------------
class Scenario(enum.Enum):
    # Localhost, same-site, cross-origin
    SCENARIO_1 = enum.auto()  # Double Submit Cookie
    SCENARIO_2 = enum.auto()  # Synchronizer Token Pattern

    # *.example.org, same-site, cross-origin
    # Require adding the following to your /etc/hosts file:
    # 127.0.0.1 api.example.org
    # 127.0.0.1 web.example.org
    SCENARIO_3 = enum.auto()  # Double Submit Cookie
    SCENARIO_4 = enum.auto()  # Synchronizer Token Pattern

    # api.example.org, myfrontend.com, cross-site,
    # Require adding the following to your /etc/hosts file:
    # 127.0.0.1 api.example.org
    # 127.0.0.1 myfrontend.com
    # Furthermore, you need to configure your browser to accept SameSite: 'None' cookies without a secure context.
    # NOTE: Modern cross-site tracking preventions mechanisms, e.g. in Safari 15, can interfere and prevent this from
    # working.
    SCENARIO_5 = enum.auto()  # Double Submit Cookie
    SCENARIO_6 = enum.auto()  # Synchronizer Token Pattern

    # Up to you to configure
    MANUAL = enum.auto()


# TODO: Change this to the scenario you want to try out. Check out the global README.md for more information.
USED_CSRF_SCENARIO: Scenario = Scenario.SCENARIO_1

if USED_CSRF_SCENARIO == Scenario.SCENARIO_1:
    CSRF_USE_SESSIONS = False
    FRONTEND_CROSS_SITE = False
    CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "http://localhost:8000"]
    CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
elif USED_CSRF_SCENARIO == Scenario.SCENARIO_2:
    CSRF_USE_SESSIONS = True
    FRONTEND_CROSS_SITE = False
    CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "http://localhost:8000"]
    CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
elif USED_CSRF_SCENARIO == Scenario.SCENARIO_3:
    CSRF_USE_SESSIONS = False
    FRONTEND_CROSS_SITE = False
    CSRF_TRUSTED_ORIGINS = ["http://web.example.org:3000", "http://api.example.org:8000"]
    CORS_ALLOWED_ORIGINS = ["http://web.example.org:3000"]
    CSRF_COOKIE_DOMAIN = ".example.org"
elif USED_CSRF_SCENARIO == Scenario.SCENARIO_4:
    CSRF_USE_SESSIONS = True
    FRONTEND_CROSS_SITE = False
    CSRF_TRUSTED_ORIGINS = ["http://web.example.org:3000", "http://api.example.org:8000"]
    CORS_ALLOWED_ORIGINS = ["http://web.example.org:3000"]
    CSRF_COOKIE_DOMAIN = ".example.org"
elif USED_CSRF_SCENARIO == Scenario.SCENARIO_5:
    CSRF_USE_SESSIONS = False
    FRONTEND_CROSS_SITE = True
    CSRF_TRUSTED_ORIGINS = ["http://myfrontend.com:3000", "http://api.example.org:8000"]
    CORS_ALLOWED_ORIGINS = ["http://myfrontend.com:3000"]
    SESSION_COOKIE_SAMESITE = "None"
    CSRF_COOKIE_SAMESITE = "None"
elif USED_CSRF_SCENARIO == Scenario.SCENARIO_6:
    CSRF_USE_SESSIONS = True
    FRONTEND_CROSS_SITE = True
    CSRF_TRUSTED_ORIGINS = ["http://myfrontend.com:3000", "http://api.example.org:8000"]
    CORS_ALLOWED_ORIGINS = ["http://myfrontend.com:3000"]
    SESSION_COOKIE_SAMESITE = "None"
    CSRF_COOKIE_SAMESITE = "None"
else:
    # Manual Configuration
    # If you want to try things outside the 4 scenarios, feel free to tinker with the settings below.

    # You can try out both the Synchronizer Token Pattern (stateful) and Double Submit Cookie (stateless) approach by
    # changing the following value. `True` for the stateful and `False` for the stateless approach.
    CSRF_USE_SESSIONS = False

    # Set this to `True` if the frontend application and the backend application are cross-site.
    FRONTEND_CROSS_SITE = False

    if CSRF_USE_SESSIONS is False:
        # If you use the stateless approach, and your frontend and backend are cross-origin (e.g. api.example.org and
        # web.example.org), you need to set the csrf cookies domain to allow the cross-origin access to the cookie with
        # the following setting (For some browsers it seems to not be needed for "localhost", even for different ports).
        #
        # The easiest way to test the stateless, cross-origin setup is to add the following to your /etc/hosts file:
        # 127.0.0.1 api.example.org
        # 127.0.0.1 web.example.org
        #
        # Don't forget to undo the changes after you are done testing

        CSRF_COOKIE_DOMAIN = ".example.org"

    # CSRF Configuration
    # https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins
    CSRF_TRUSTED_ORIGINS = []

    # Configuration for cross-origin setups
    # https://github.com/adamchainz/django-cors-headers
    CORS_ALLOWED_ORIGINS = []

# ---------------------------------------------------------------------------------------------------------------------

# Please don't change the following settings unless you now what you do

# Whether the login API endpoints should contain a CSRF token or not.
# Required when `CSRF_USE_SESSIONS` is set to `True` (stateful approach).
# In case `CSRF_USE_SESSIONS` is `False`, we also need to return the CSRF token in the response, because the frontend
# application cannot read a cookie cross-site.
CSRF_TOKEN_IN_RESPONSE_BODY = FRONTEND_CROSS_SITE or CSRF_USE_SESSIONS

# Tells the frontend, using cors headers, that it should send along cookies.
CORS_ALLOW_CREDENTIALS = True