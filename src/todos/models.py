from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item": "Example schema!",
                    "status": "successfully"
                }
            }
        }


class TodoItem(BaseModel):
    item: Item

    class Config:
        json_schema_extra = {
            "example": {
                "item": {
                    "item": "Read the next chapter of the book",
                    "status": "successfully"
                }
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": {
                            "item": "Example schema 1!",
                            "status": "Example status"
                        }
                    },
                ]
            }
        }
