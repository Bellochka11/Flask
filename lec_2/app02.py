from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from forms import LoginForm, RegistrationForm
from flask_wtf.csrf import CSRFProtect

#генерация надежного секретного ключа
# пайтон консоль пишем в терминале в вс коде python, зачем эти команды:
# >>> import secrets
# >>> secrets.token_hex()

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'mysecretkey' #защита от сетевых атак шифрование данных форм
app.config['SECRET_KEY'] = b'f117a01a15f0f7e9136e048cc9a54a486ae3e9ab5d329db72c1e5910d37ba32d' #защита от сетевых атак шифрование данных форм
csrf = CSRFProtect(app) #инициализация



@app.route('/')
def index():
    return 'Hi'

# @app.route('/form', methods=['GET', 'POST']) #пишем /form
# @csrf.exempt #форма без токена без секретного ключа не защищенная!!!!!!!!!!!!!!!
# def my_form():
#     return 'No CSRF protection'



@app.route('/login/', methods=['GET', 'POST']) #принимает гет и пост запросы /login/'
def login():
    form = LoginForm() #экземпляр LoginForm
    if request.method == 'POST' and form.validate(): #form.validate() форма прошла валидация проверки
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form) #гет запрос


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm() #экземпляр RegistrationForm
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data #извлекаем данные из формы на сайте
        password = form.password.data
        print(email, password)
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()
