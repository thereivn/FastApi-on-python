from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    item: str

class Todo(BaseModel):
    id: Optional[int]
    item: Item
    
    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(id=None, item=Item(item=item)) 

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item": "Example schema!"
                }
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = { 
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"}
                ]
            }
        }

