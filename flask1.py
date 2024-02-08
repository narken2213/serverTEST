from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    with open('templates/index.html', 'r', encoding='utf-8') as stream:
        return stream.read()
@app.route('/index')
def index1():
    with open('templates/index2.html', 'r', encoding='utf-8') as stream:
        return stream.read()
@app.route('/promotion')
def index2():
    with open('templates/index3.html', 'r', encoding='utf-8') as stream:
        return stream.read()
@app.route('/image_mars')
def index3():
    with open('templates/index4.html', 'r', encoding='utf-8') as stream:
        return stream.read()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)