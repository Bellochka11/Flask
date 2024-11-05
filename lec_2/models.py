from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #колонка для таблицы первичный ключ
    username = db.Column(db.String(80), unique=True, nullable=False) #колонка для юзернайм unique=True поле уникальное не может быть два одинаковых  nullable=False поле не пустое
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # default=datetime.utcnow записывает текущ время
    posts = db.relationship('Post', backref='author', lazy=True)
    # db.relationship('Post' один юзер может написать несколько статей пост
    # lazy=True экономим вычислит ресурсы
    
    def __repr__(self):
        return f'User({self.username}, {self.email})'
    
    
class Post(db.Model): #текст какой то статьи
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'),
    nullable=False)
    #db.ForeignKey('user.id') ссылаться на таблицу User.id
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'Post({self.title}, {self.content})'
    
    
class Comment(db.Model): #комментарий к статьям
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False) #db.ForeignKey('post.id') ссылаться на таблицу post.id
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'),
    nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'Comment({self.content})'