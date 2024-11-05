from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>/') # http://127.0.0.1:5000/liza/
def hello(name='незнакомец'):
    return f'Привет, {name.capitalize()}!' # Привет, Liza!

@app.route('/file/<path:file>/') # http://127.0.0.1:5000/file/llsls%5B/xcls/;lda/
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"' #Путь до файла "llsls[/xcls/;lda"   <class 'str'>

@app.route('/number/<float:num>/') # http://127.0.0.1:5000/number/7.8/
def set_number(num):
    print(type(num))
    return f'Передано число {num}' # Передано число 7.8     <class 'float'>


@app.route('/')
def index():
    return 'Привет, незнакомецыы!'

@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'

@app.route('/Иван/')
def ivan():
    return 'Привет, Ванечка!'

@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Феодор!'


if __name__ == '__main__':
    app.run(debug=True)
