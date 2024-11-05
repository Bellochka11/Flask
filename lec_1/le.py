from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return escape('Hello Worldddssa!')

if __name__ == '__main__':
    app.run()
