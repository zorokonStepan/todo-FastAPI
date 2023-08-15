from fastapi import APIRouter, Path

from src.models import Todo, TodoItem


todo_router = APIRouter()


# todo_list = []
todo_list = [
    {
        "id": 0,
        "item": {
            "item": "Example schema 0!",
            "status": "successfully",
        }
    },
    {
        "id": 1,
        "item": {
            "item": "Example schema 1!",
            "status": "successfully",
        }
    },
    {
        "id": 2,
        "item": {
            "item": "Example schema 2!",
            "status": "successfully",
        }
    },
    {
        "id": 3,
        "item": {
            "item": "Example schema 3!",
            "status": "successfully",
        }
    },
]


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"src": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo with supplied ID doesn't exist."}


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully."}
    return {"message": "Todo with supplied ID doesn't exist."}
