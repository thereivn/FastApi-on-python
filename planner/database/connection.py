from beanie import PydanticObjectId, init_beanie
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient 
from typing import Any, List, Optional
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from models.users import User
from models.events import Event
class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    
    async def initialize_database(self):
        try:
            client = AsyncIOMotorClient(self.DATABASE_URL)
            await init_beanie(database=client.get_default_database(), document_models=[Event, User])
        except Exception as e:
            print(f"Error initializing database: {e}")
    class Config:
        env_file = ".env"

class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return
    
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc
    
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list() 
        return docs
    
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        try:
            des_body = body.dict(exclude_unset=True)
            update_query = {"$set": {field: value for field, value in des_body.items()}}
            
            doc = await self.get(id)  # Получаем документ
            if not doc:
                raise HTTPException(status_code=404, detail="Document not found")
            
            await doc.update(update_query)
            return doc  # Возвращаем обновлённый документ
        except Exception as e:
            print(f"Error updating document: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
        
    async def delete(self, id: PydanticObjectId) -> bool: 
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True