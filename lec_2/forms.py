from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm): #каждый класс будет наследоваться от  FlaskForm
    username = StringField('Username', validators=[DataRequired()]) #validators=[DataRequired()] - данные нужно заполнить если не заполнит форма будет не принята
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])

class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(), Email()]) #должен быть похож на емэил
    password=PasswordField('Password',validators=[DataRequired(), Length(min=6)]) #длина минимум 6
    confirm_password=PasswordField('ConfirmPassword',validators=[DataRequired(), EqualTo('password')]) #поля должны совпадать с password