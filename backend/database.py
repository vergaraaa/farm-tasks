from models import Task
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost")
database = client.farm_tasks
collection = database.tasks

async def get_one_task_id(id):
    task = await collection.find_one({"_id": id})
    return task


async def get_all_tasks():
    tasks = []
    cursor = await collection.find({})
    async for doc in cursor:
        tasks.append(Task(**doc))

    return tasks

async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({"_id": new_task.inserted_id})

    return created_task


async def update_task(id: str, task):
    await collection.update_one({"_id": id}, {'$set': task})
    updated_task = await collection.find_one({"_id": id})

    return updated_task

async def delete_task(id: str):
    await collection.delete_one({"_id": id})
    return True