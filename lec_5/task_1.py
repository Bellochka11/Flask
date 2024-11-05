from typing import List #список данных
from fastapi import FastAPI
from pydantic import BaseModel, Field

# uvicorn lec_5.task_1:app --reload   запуск приложения из папки Flask app в 6 строке
app = FastAPI() #приложение

class Item(BaseModel): #класс модели
    name: str
    price: float 
    is_offer: bool = None

class User(BaseModel):#класс модели
    username: str
    full_name: str = None

class Order(BaseModel):#класс модели
    items: List[Item] #список лист в нем каждый элемент экземпляр Item
    user: User #экземпляр юзер


class Item(BaseModel):
    name: str = Field(max_length=10) # Field вместо значения по умолчанию

class User(BaseModel):
    age: int = Field(default=0) # Field вместо значения по умолчанию




class User(BaseModel):
    username: str = Field(title="Username", max_length=50)
    full_name: str = Field(None, title="Full Name", max_length=100) # None по умолчанию

class Item(BaseModel):
    name: str = Field(..., title="Name", max_length=50) #... - поля обязательное title="Name" - будет использоваться в документации заголовок
    price: float = Field(..., title="Price", gt=0, le=100000) #gt=0 - price должно быть больше 0. 0 не включаем. le=100000 - меньше или равно le
    description: str = Field(default=None, title="Description", max_length=1000)
    tax: float = Field(0, title="Tax", ge=0, le=10) # 0 - значение по умолчанию ge=0 - меньше или равно 0


@app.post("/items/")
async def create_item(item: Item): #на вход json объект может сформировать item
    return {"item": item}