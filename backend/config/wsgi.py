"""
WSGI config for PredictStats project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set production settings by default
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

# WhiteNoise application wrapper for static files
application = get_wsgi_application()

# Apply WhiteNoise middleware in production
try:
    from whitenoise import WhiteNoise
    application = WhiteNoise(
        application,
        root=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles'),
        prefix='static/',
        max_age=31536000  # 1 year cache
    )
except ImportError:
    pass  # Dev environment doesn't need WhiteNoise
