from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-only-secret-key"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cityinfo",
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

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "uk-ua"
TIME_ZONE = "Europe/Kyiv"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media files (uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Custom settings for external URLs
PRIMARY_CITY_SITE = os.environ.get("PRIMARY_CITY_SITE", "https://shargorod-miskrada.gov.ua")
SHARGOROD_NET_SITE = os.environ.get("SHARGOROD_NET_SITE", "https://shargorod.net")
LEADERSHIP_PAGE_SLUG = os.environ.get("LEADERSHIP_PAGE_SLUG", "kerivniĭ-sklad-15-22-24-16-02-2017/")
ALBUM_PAGE_SLUG = os.environ.get("ALBUM_PAGE_SLUG", "album/6833/")

LEADERSHIP_URLS = [
    os.environ.get("LEADERSHIP_URL_1", "https://shargorod-miskrada.gov.ua/shargorodskij-miskij-golova-bareckij-volodimir-ivanovich-10-43-46-15-01-2021/"),
    os.environ.get("LEADERSHIP_URL_2", "https://shargorod-miskrada.gov.ua/sekretar-shargorodskoi-miskoi-radi-kedik-katerina-stanislavivna-10-47-21-15-01-2021/"),
    os.environ.get("LEADERSHIP_URL_3", "https://shargorod-miskrada.gov.ua/zastupnik-golovi-miskoi-radi-solyanik-artem-sergijovich-10-59-21-15-01-2021/"),
    os.environ.get("LEADERSHIP_URL_4", "https://shargorod-miskrada.gov.ua/zastupnik-golovi-miskoi-radi-majdanjuk-andrij-antonovich-11-01-30-15-01-2021/"),
    os.environ.get("LEADERSHIP_URL_5", "https://shargorod-miskrada.gov.ua/kerujuchij-spravami-vikonavchogo-komitetu-kushnir-igor-petrovich-11-04-57-15-01-2021/"),
]
