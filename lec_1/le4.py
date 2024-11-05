from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/users/')
def users():
    _users = [{'name': 'Никанор',
                'mail': 'nik@mail.ru',
                'phone': '+7-987-654-32-10',
                },
                {'name': 'Феофан',
                'mail': 'feo@mail.ru',
                'phone': '+7-987-444-33-22',
                },
                {'name': 'Оверран',
                'mail': 'forest@mail.ru',
                'phone': '+7-903-333-33-33',
                }, ]
    context = {'users': _users,
               'title':'точечная нотация'}
    return render_template('users.html', **context)

@app.route('/for/')
def for_show():
    context = { 'title':'цикл',
                'poem': ['Вот не думал, не гадал,',
                'Программистом взял и стал.',
                'Хитрый знает он язык,',
                'Он к другому не привык.',
            ]}
    # txt = """<h1>Стихотворение</h1>\n<p>""" + '<br/>'.join(poem) + '</p>'
    return render_template('for_show.html', **context)

@app.route('/if/')
def if_show():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон',
        'user':'llf',
        'number': 2
    }
    return render_template('if_show.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
