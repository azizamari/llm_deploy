import os

from dotenv import load_dotenv
load_dotenv() 

class RedisConfig:
    HOST = os.environ.get("REDIS_HOST", None)
    PORT = os.environ.get("REDIS_PORT", None)

class CeleryTasksGeneralConfig:

    broker_url = os.environ.get("CELERY_BROKER_URL", None)
    result_backend = os.environ.get("CELERY_RESULT_BACKEND", None)

class HuggingFaceConfig:
    token = os.environ.get("HUGGING_FACE", None)