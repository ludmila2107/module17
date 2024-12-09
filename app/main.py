from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router, prefix="/task", tags=["task"])
app.include_router(user_router, prefix="/user", tags=["user"])