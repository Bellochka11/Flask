import logging
from pathlib import PurePath, Path
from flask import Flask, redirect, url_for, request, flash, render_template
from werkzeug.utils import secure_filename #безопасное имя функции

app = Flask(__name__)

#генерация надежного секретного ключа
# пайтон консоль пишем в терминале python
# >>> import secrets
# >>> secrets.token_hex()

app.secret_key =b'37f73934ef495c0806d8c78a2526ed14c9270ab26c0936eea09a59d4edffd12b'

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         # Обработка данных формы
#         flash('Форма успешно отправлена!', 'success')
#         return redirect(url_for('form'))
#     return render_template('flash_form.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST': # если не ввели имя в форме выведет  Введите имя
    # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'

@app.route('/redirect/') # http://127.0.0.1:5000/redirect перенаправит на http://127.0.0.1:5000
def redirect_to_index():
    return redirect(url_for('index'))

@app.route('/external')
def external_redirect():
    return redirect('https://google.com') # https://www.google.com/

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'

@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
