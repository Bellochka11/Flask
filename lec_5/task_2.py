import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

# uvicorn lec_5.task_2:app --reload   запуск приложения из папки Flask app в 6 строке

DATABASE_URL = "sqlite:///lec_5/mydatabase.db" #в папке создаем бд


database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData() #метаданные

# engine = sqlalchemy.create_engine(DATABASE_URL) #создаем движок сделали это и mydatabase появилась пустая
# metadata.create_all(engine) #сформируем таблицы в бд

users = sqlalchemy.Table( #создали таблицу
        "users", #название таблицы
        metadata, #метаданные 13
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), # стролбцы primary_key=True первичный ключ
        sqlalchemy.Column("name", sqlalchemy.String(32)),
        sqlalchemy.Column("email", sqlalchemy.String(128)),
)

engine = sqlalchemy.create_engine( #создаем движок
    DATABASE_URL, connect_args={"check_same_thread": False} # "check_same_thread": False - бд sqlite нужен
)
metadata.create_all(engine)#сформируем таблицы в бд



app = FastAPI()

class UserIn(BaseModel): #добавление данных нет id но присваивается автоматически
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

class User(BaseModel): #чтение данных т.к. есть id
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# @app.get("/fake_users/{count}") #заполняем таблицу фейковыми данными для примера
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru') #сформировали пользователей
#         await database.execute(query) #асинхронный запрос к бд добавляем пользователей
#     return {'message': f'{count} fake users create'}

#Создание пользователя в БД, create
@app.post("/users/", response_model=User) #response_model=User вернем юзер
async def create_user(user: UserIn): #МОДЕЛЬ UserIn
    query = users.insert().values(name=user.name, email=user.email) #ОБЪЕКТ ЗАПРОСА users - ТАБЛИЦА insert() - ДОБАВЛЕНИЕ НОВЫХ ДАННЫХ В ТАБЛИЦУ
    # query = users.insert().values(**user.dict()) # то же самое что и в 55 строчке
    last_record_id = await database.execute(query) #execute-выполняем query, сохранен id нашей записи
    return {**user.dict(), "id": last_record_id}

# Чтение всех пользователей из БД,read
@app.get("/users/", response_model=List[User]) #возвращаем список пользователей
async def read_users():
    query = users.select() #выбери всех из таблицы users
    return await database.fetch_all(query) #fetch_all - верни всех в виде списка

# Чтение одного пользователя из БД,read
@app.get("/users/{user_id}", response_model=User) #возвращаем 1 пользователя /users/5
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id) # where где c - колонка 
    return await database.fetch_one(query) #верни 1 пользователя

# Обновление пользователя в БД, update
@app.put("/users/{user_id}", response_model=User) #возвращаем 1 пользователя /users/5
async def update_user(user_id: int, new_user: UserIn): #new_user: UserIn должно совпадать
    query = users.update().where(users.c.id == user_id).values(**new_user.dict()) #нашли пользователя с определенным user_id возьми нового пользователя преврати его в словарь распакуй его имя по ключу нейм и почту по емэил и присвой это пользователю с user_id
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


# Удаление пользователя из БД,delete
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id) #удаляем пользователя где user_id
    await database.execute(query)
    return {'message': 'User deleted'}









@app.on_event("startup") #сработает по опредленному событию а не когда пользователь перейдет по адресу запуск приложения
async def startup():
    await database.connect() #подключаемся к бд

@app.on_event("shutdown") #выключение сервера 
async def shutdown():
    await database.disconnect() #отключиться