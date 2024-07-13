from celery_setup import celery_app
import time

@celery_app.task
def add(x, y):
    # block for 10 seconds
    time.sleep(10)
    return x + y

@celery_app.task
def llm_inference():
    # Example: Simulate LLM inference process
    time.sleep(5)  # Replace with actual LLM inference logic
    return "LLM inference completed."