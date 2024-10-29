from fastapi import FastAPI
from apirout import todo_router

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определяем маршрут для приветствия
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

# Дополнительный маршрут, например, для проверки статуса
@app.get("/status")
async def status() -> dict:
    return {"status": "running"}

app.include_router(todo_router)