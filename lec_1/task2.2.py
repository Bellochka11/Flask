import logging
from pathlib import PurePath, Path
from flask import Flask, request, render_template, abort
from werkzeug.utils import secure_filename #безопасное имя функции

app = Flask(__name__)

logger = logging.getLogger(__name__)

@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500

def get_blog(id):
    return None

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)
# возвращаем найденную в БД статью

@app.errorhandler(404)
def page_not_found(e): #обработка ошибки 404
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url, #адрес то что пользователь ввел в командной строке
    }
    return render_template('404.html', **context), 404

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'Flask', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
