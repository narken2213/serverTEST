import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def index1(prof):
    return render_template('trainig.html', prof=prof)

@app.route('/list_prof/<marker>')
def index2(marker):
    with open("prof.json", "rt", encoding="utf8") as f:
        prof_list = json.loads(f.read())
    print(prof_list)
    return render_template('news.html', marker=marker, prof_list = prof_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777)