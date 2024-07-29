# LLM Deployment with FastAPI, Celery, Redis, and MLflow

![image](https://github.com/user-attachments/assets/8b929152-4f63-4774-a434-cf462a813f13)

This project demonstrates how to deploy a Large Language Model (LLM) as an API using FastAPI, Celery, and Redis, while leveraging MLflow for model registry and Hugging Face for model sourcing. The setup includes Docker configurations to run FastAPI, Celery, and Redis as separate containers.

## Prerequisites

- Docker
- Docker Compose
- Redis

## Setup

### Environment Variables

```
REDIS_HOST=redis
REDIS_PORT=6379
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
MLFLOW_TRACKING_URI=http://mlflow:5000
HUGGING_FACE= your hugging face read token
```

### Installation and Running

1. **Build and Start Docker Containers**

```bash
docker-compose up --build
```

2. **Access the FastAPI Documentation**

Open your browser and navigate to http://localhost:8000/docs to access the FastAPI interactive API documentation.


