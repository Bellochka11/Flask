import logging
from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI() #создали приложение

# uvicorn lec_4.task_1:app --reload   запуск приложения из папки Flask app в 4 строке

#на локальном сервере есть JSON объект "message": "Hello World" пересылка сообщений от сервера к клиенту и наоборот

class Item(BaseModel): #базовая модель
    name: str
    description: Optional[str] = None #описане опциональная строка по умолчанию нон но ожидаем строку Optional - переменная не обязательная
    price: float
    tax: Optional[float] = None #скидка наценка опциональная флот по умолчанию нон но ожидаем флот


# @app.get("/") #гет запрос на сервер декоратор
# async def read_root(): #асинхронная функция корутина возвращает словарь
#     logger.info('Отработал GET запрос.')
#     return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q:str = None):
    if q:
        return{"item_id":item_id,"q":q}
    return{"item_id":item_id}

# @app.get("/items/{item_id}") # /items/42 если хочу передать q то пишу: /items/42?q=text
# async def read_item(item_id: int, q: str = None): #item_id: int инт q: str = None стр по умолчанию нон
#     return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}/orders/{order_id}") #/users/1/orders/2
async def read_item(user_id:int,order_id:int):
    #обработка данных
    return{"user_id":user_id,"order_id":order_id}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): #выборка из бд пропусти 100 записей и выдай 50, /items/?limit=4&skip=3 - 2 параметра, /items/?limit=4 - 1 параметр
    return {"skip": skip, "limit": limit}

@app.get("/", response_class=HTMLResponse) #возвращает текст
async def read_root():
    return "<h1>Hello World</h1>"

@app.get("/message") #json
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200) #возвращает код 200


@app.post("/items/") #пост запрос новые данные
async def create_item(item: Item): #item объект который хотим получить из пост запроса
    logger.info('Отработал POST запрос.')
    return item


@app.put("/items/{item_id}") #обновление данных на сервере
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}") #удаление данных с сервера удаляем строку в бд
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}


templates = Jinja2Templates(directory="./lec_4/templates")

@app.get("/{name}", response_class=HTMLResponse) #/liza
async def read_item(request: Request, name: str):
    print(request)
    return templates.TemplateResponse("item.html", {"request": request, "name": name}) #"request": request запрос ответ