from fastapi import APIRouter, Path, HTTPException
from model import Todo, TodoItem

todo_router = APIRouter()
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "Put " and todo and " with message": "Todo added successfully."
    }

@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {
        "Get " and todo_list and " from todos": todo_list
    }


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": {
                    "id": todo.id,
                    "item": todo.item.item,
                    "status": todo.item.status
                }
            }
    raise HTTPException(status_code=404, detail="Todo with supplied ID doesn't exist.")
    # return {
    #     "message": "Todo with supplied ID doesn't exist."
    # }

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item.item = todo_data.item 
            todo.item.status = todo_data.status
            return {
                "message": "Todo updated successfully."
                }
    raise HTTPException(status_code=404, detail="Todo with supplied ID doesn't exist.")
    # return {
    # "message": "Todo with supplied ID doesn't exist."
    # }   