from fastapi import FastAPI

from src.main.handlers import main_router
from src.todos.handlers import todo_router

app = FastAPI()

app.include_router(main_router)
app.include_router(todo_router)
