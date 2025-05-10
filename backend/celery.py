import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

app = Celery('PredictStats')

# Configure using Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Redis connection configuration
app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.result_backend = settings.CELERY_RESULT_BACKEND
app.conf.broker_connection_retry_on_startup = True

# Task timeouts and retry policy
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'tasks'
app.conf.task_default_routing_key = 'task.default'
app.conf.task_soft_time_limit = 600  # 10 minutes
app.conf.task_time_limit = 1200       # 20 minutes
app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True

# Scheduled tasks (Celery Beat)
app.conf.beat_schedule = {
    'daily-prediction-update': {
        'task': 'core.tasks.daily_prediction_update',
        'schedule': 3600 * 24,  # Every 24 hours
        'options': {
            'queue': 'periodic'
        }
    },
    'retrain-models-weekly': {
        'task': 'prediction_engine.tasks.retrain_models',
        'schedule': 3600 * 24 * 7,  # Weekly
        'options': {
            'queue': 'heavy_tasks'
        }
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Health check endpoint
@app.task(name='celery.ping')
def ping():
    return 'pong'
