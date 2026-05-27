from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent #Це базова папка проєкту.

SECRET_KEY = "dev-only-secret-key" #Це секретний ключ Django.

DEBUG = True # Django показує детальні помилки
ALLOWED_HOSTS = ["*"] #Це список доменів/хостів, з яких Django дозволяє запити. У режимі розробки можна використовувати ["*"], але в продакшені потрібно вказати конкретні домени.

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "feachers",
] #Це список підключених додатків.

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]#Middleware — це “шари” обробки запиту між браузером і view. Вони можуть виконувати різні функції, такі як обробка сесій, аутентифікація, захист від CSRF та інші.

ROOT_URLCONF = "core.urls"#Це головний файл маршрутів. Він вказує Django, де шукати маршрути для обробки запитів. У цьому випадку він вказує на файл core/urls.py.

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
]# Це налаштування шаблонів. Вказує, що ми використовуємо стандартний бекенд Django для шаблонів, дозволяємо автоматичне знаходження шаблонів у папках додатків (APP_DIRS=True) і визначаємо контекстні процесори, які додають змінні до контексту шаблонів.

#Це точки входу для серверів:
WSGI_APPLICATION = "core.wsgi.application" # WSGI — класичний синхронний режим
ASGI_APPLICATION = "core.asgi.application" # ASGI — сучасний async-режим

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}# Це налаштування бази даних. У цьому випадку ми використовуємо SQLite, яка зберігає дані у файлі db.sqlite3 в кореневій папці проєкту. Для продакшена зазвичай використовують більш потужні бази даних, такі як PostgreSQL або MySQL.

AUTH_PASSWORD_VALIDATORS = []#Перевірки паролів для користувачів. Порожньо — означає, що валідація вимкнена.

LANGUAGE_CODE = "uk-ua" #Мова інтерфейсу Django.
TIME_ZONE = "Europe/Kyiv" #Часовий пояс проєкту.
#USE_I18N — підтримка інтернаціоналізації
#USE_TZ — зберігати/обробляти час з часовими зонами
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"#Базовий URL для статичних файлів: CSS, JavaScript, зображення тощо. У режимі розробки Django автоматично обслуговує файли з цієї URL, але в продакшені потрібно налаштувати веб-сервер для обслуговування статичних файлів.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"#Яке поле Django використовує для primary key за замовчуванням у моделях.

