from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    done: bool

tasks = [
    Task(id=1, title="Buy milk", done=False),
    Task(id=2, title="Walk the dog", done=True),
    Task(id=3, title="Finish assignment", done=False),
]

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")