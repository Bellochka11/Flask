import logging
from pathlib import PurePath, Path
from flask import Flask, request, make_response, render_template, session, redirect, url_for

app = Flask(__name__)

app.secret_key ='3f35b0fba198cce55f3d51abf0c2f5bc4263d35c5fdc85a11b05b83ef1f6e854'

@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))
    
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName' # если отправил без ввода в полях имя то вылезет привет ноу нейм
        return redirect(url_for('index'))
    return render_template('username_reg.html')

@app.route('/logout/')
def logout():
    session.pop('username', None) #удалили сессию
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)