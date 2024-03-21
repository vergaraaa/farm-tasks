from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome(): 
    return { "message": "welcome to my fastapi api"}

@app.get("/api/tasks")
async def get_tasks(): 
    return "all tasks"

@app.post("/api/tasks")
async def create_task(): 
    return "create task"

@app.get("/api/tasks/{id}")
async def get_task(): 
    return "single tasks"

@app.put("/api/tasks/{id}")
async def update_task(): 
    return "updating task"

@app.delete("/api/tasks/{id}")
async def delete_task(): 
    return "delete task"