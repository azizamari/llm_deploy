from fastapi import FastAPI, BackgroundTasks
from celery.result import AsyncResult
from celery import Celery
import config


app = FastAPI()
celery_app = Celery(
    'worker',
    broker=config.CeleryTasksGeneralConfig.broker_url,
    backend=config.CeleryTasksGeneralConfig.result_backend,
)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Celery and Redis"}

@app.post("/add/{x}/{y}")
async def add_numbers(x: int, y: int):
    task = celery_app.send_task('tasks.add', args=[x, y])
    return {"message": f"Task to add {x} and {y} sent to Celery worker.", "task_id": task.id}


@app.get("/status/{task_id}")
def get_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    if result.state == 'PENDING':
        response = {
            "state": result.state,
            "status": "Pending..."
        }
    elif result.state != 'FAILURE':
        response = {
            "state": result.state,
            "result": result.result
        }
    else:
        response = {
            "state": result.state,
            "status": str(result.info),  # this is the exception raised
        }
    return response
