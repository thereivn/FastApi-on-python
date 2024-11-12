from pydantic import BaseModel, EmailStr 
from typing import Optional, List
from models.events import Event
class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]
    username: str

    class Config:
        schema_extra = {
            "example": {
            "email": "fastapi@packt.com",
            "username": "strong!!!",
            "events": [],
            }
        }

class NewUser(User):
    password: Optional[str] = None  # Убираем обязательность поля password
    events: Optional[List[Event]] = None  # Делаем events необязательным

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "events": [],
            }
        }

class UserSignIn(BaseModel):
        email: EmailStr 
        password: str
        class Config:
            schema_extra = {
            "example": {
            "email": "fastapi@packt.com",
            "password": "strong!!!",
            "events": [],
            }
    }