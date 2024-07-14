from celery_setup import celery_app
import time

@celery_app.task
def add(x, y):
    # block for 10 seconds
    time.sleep(10)
    return x + y

@celery_app.task
def llm_inference():
    # fetch model from mlflow model registry and perform inference
    pass