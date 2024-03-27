from fastapi import FastAPI, HTTPException
from database import get_all_tasks, create_task
from models import Task

app = FastAPI()

@app.get("/")
def welcome(): 
    return { "message": "welcome to my fastapi api"}

@app.get("/api/tasks")
async def get_tasks(): 
    tasks = await get_all_tasks()
    return tasks

@app.post("/api/tasks", response_model=Task)
async def save_task(task: Task): 
    newTask = await create_task(task.model_dump())

    if newTask: 
        return newTask
    
    raise HTTPException(400, "Something went wrong")


# @app.get("/api/tasks/{id}")
# async def get_task(): 
#     return "single tasks"

# @app.put("/api/tasks/{id}")
# async def update_task(): 
#     return "updating task"

# @app.delete("/api/tasks/{id}")
# async def delete_task(): 
#     return "delete task"