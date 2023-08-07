from fastapi import FastAPI

from todos.todo import todo_router


app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello!"}

app.include_router(todo_router)
