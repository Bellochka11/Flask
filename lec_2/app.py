from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Post, Comment
import os
from datetime import datetime, timedelta
app = Flask(__name__) #инициируем приложение
# в файл конфигурации лобавляю константу и значение
# в instance будет храниться вся прослойка бд


# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'mydatabase.db')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/mydatabase.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/mydatabase.db'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'mydatabase.db')


# можем подключить любую бд
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/database_name'

db.init_app(app) #инициируем приложение связали бд и фласк

@app.route('/')
def index():
    return 'Hi'

@app.route('/data/')
def data():
    return 'Your data'

# Получение данных из базы данных
@app.route('/users/')
def all_users():
    # return 'Your user'
    users = User.query.all() # all() - все пользователи из бд
    context = {'users': users}
    return render_template('users.html', **context) 

#ФИЛЬТРАЦИЯ ДАННЫХ ИЗ БД
@app.route('/users/<username>/') #<username> имя в бд например /users/user2/
def users_by_username(username):
    users = User.query.filter(User.username == username).all() #найди юзернейм который совпадает с тем который мы передали в <username> all() - все такие юзеры
    context = {'users': users}
    return render_template('users.html', **context)

#ФИЛЬТРАЦИЯ ДАННЫХ ИЗ БД
@app.route('/posts/author/<int:user_id>/') #/posts/author/3/ пример вместо 3 можно выбрать id юзера
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all() #найди author_id который совпадает с тем который мы передали в <int:user_id> all() - все такие юзеры
    if posts: #если в посте есть информация
        # возвращает информацию в виде json
        return jsonify(
            [{'id': post.id, 'title': post.title,
                'content': post.content, 'created_at': post.created_at} for post in
                posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404 #/posts/author/33/ передаем несуществующее id автора получаем 'error': 'Posts not found'
    
#ФИЛЬТРАЦИЯ ДАННЫХ ИЗ БД    
@app.route('/posts/last-week/') # пишем /posts/last-week/
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7) #от текущ времени отнимаем семь дней
    posts = Post.query.filter(Post.created_at >= date).all() #отфильтруй посты которые были созданы за последние 7 дней all() - все
    if posts: #если в посте есть информация
        return jsonify([{'id': post.id, 'title': post.title,
                          'content': post.content, 'created_at': post.created_at} for post
                            in posts])
    else:
        return jsonify({'error': 'Posts not found'})

# cli.command в консоли запускаем команды

#СОЗДАНИЕ БД
@app.cli.command("init-db") # запускаем flask init-db в директории в которой мы находимся
 # в файле wsgi должно быть from app01 import app
def init_db():
    db.create_all() #создать таблицы  на основе моделей
    print('OK')

#ДОБАВЛЕНИЕ
@app.cli.command("add-john") # запускаем flask add-john в директории в которой мы находимся
def add_user():
    # создаю экземпляр класса юзер и присваиваю поля
    user = User(username='john', email='john@example.com')
    db.session.add(user) #подключение добавляем пользователя подгтовка к фиксации
    db.session.commit() #строка в бд фиксация
    print('John add in DB!')

# ИЗМЕНЕНИЕ
@app.cli.command("edit-john") #flask edit-john
def edit_user(): 
    user=User.query.filter_by(username='john').first() #запрос на чтение объект запроса отфильтруй по юзернейм first() - первого в поиске
    user.email='new_email@example.com' #изменение
    db.session.commit() #фиксация
    print('EditJohnmailinDB!')

#УДАЛЕНИЕ 
@app.cli.command("del-john") # flask del-john
def del_user():
    user = User.query.filter_by(username='john').first()#запрос на чтение объект запроса отфильтруй по юзернейм first() - первого в поиске
    db.session.delete(user) #УДАЛЕНИЕ
    db.session.commit()#фиксация
    print('Delete John from DB!')

#НАПОЛНИЛИ БД ПОЛЬЗОВАТЕЛЯМИ
@app.cli.command("fill-db") # flask fill-db
def fill_tables(): # ЗАПОЛНИ ТАБЛИЦУ
    count = 5
    # Добавляем 5 пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit() #фиксация

    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}',
        content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()#фиксация






if __name__ == '__main__':
    app.run()
