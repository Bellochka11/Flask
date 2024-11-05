from flask import Flask, request, render_template

app = Flask(__name__)

@app.get('/submit')
def submit_get():
    return render_template('subm.html')

@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'

@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
        # http://127.0.0.1:5000/get/?name=alex&age=13&level=80
        # Похоже ты опытный игрок, раз имеешь уровень 80
        # ImmutableMultiDict([('name', 'alex'), ('age', '13'), ('level', '80')])
    else:
        text = 'Привет, новичок.<br>'
        # http://127.0.0.1:5000/get/
        # Привет, новичок.
        # ImmutableMultiDict([])
    return text + f'{request.args}'


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('subm.html')


if __name__ == '__main__':
    app.run(debug=True)

