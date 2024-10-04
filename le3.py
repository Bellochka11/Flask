from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/index/') # http://127.0.0.1:5000/index/
def index():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон',
    }
    return render_template('indexs.html', **context) # Привет, меня зовут Харитон подставится name Харитон


# @app.route('/index/') #http://127.0.0.1:5000/index/
# def html_index():
#     return render_template('indexs.html') # indexs.html - имя файла с кодом html.  indexs.html ОБЯЗАТЕЛЬНО лежит в папке templates

html = """
<h1>Привет, меня зовут Алексей</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""
@app.route('/text/') # http://127.0.0.1:5000/text/
def text():
    return html # Привет, меня зовут Алексей Уже много лет я создаю сайты на Flask. Посмотрите на мой сайт.

@app.route('/poems/') # http://127.0.0.1:5000/poems/
def poems():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
        ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) +'</p>'
    return txt # Стихотворение Вот не думал, не гадал, Программистом взял и стал. Хитрый знает он язык, Он к другому не привык.

if __name__ == '__main__':
    app.run(debug=True)
