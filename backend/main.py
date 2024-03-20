from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome(): 
    return { "message": "welcome to my fastapi api"}