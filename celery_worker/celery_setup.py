from celery import Celery
import config

# Configure Celery to use Redis as the broker
celery_app = Celery(
    'worker',
    broker=config.CeleryTasksGeneralConfig.broker_url,
    backend=config.CeleryTasksGeneralConfig.result_backend,
    broker_connection_retry_on_startup=True,
    include=['tasks']
)

celery_app.conf.update(
    result_expires=3600,
    task_routes={
        'tasks.add': {'queue': 'default'},
        'tasks.llm_inference': {'queue': 'default'},
    }
)

