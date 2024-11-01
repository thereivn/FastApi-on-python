from pydantic import BaseModel

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item": "Example schema!",
                    "status": "nothing to do"
                }
            }
        }

class TodoItem(BaseModel):
    item: Item

    class Config:
        schema_extra = { 
                "example":{
                    "item": {
                        "item": "Read the next chapter of the book",
                        "status": "in progress"
                    }
                    # "item": "Read the next chapter of the book"
                    # }
                }
        }
