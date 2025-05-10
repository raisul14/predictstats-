from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# ডেভেলপমেন্ট টুলস
INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# ডাটাবেস কনফিগ (SQLite)
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'dev_db.sqlite3',
}

# ডিবাগ টুলবার
INTERNAL_IPS = [
    '127.0.0.1',
]

# কনসোলে ইমেইল লগিং
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CORS সেটিংস
CORS_ALLOW_ALL_ORIGINS = True

# লগিং কনফিগ
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
