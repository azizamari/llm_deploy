# Dockerfile for Celery worker
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "celery_setup.celery_app", "worker", "--loglevel=info"]
