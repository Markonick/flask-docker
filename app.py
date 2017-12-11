from flask import Flask
from flask import render_template
from redis import Redis
import pandas as pd


app = Flask(__name__, template_folder='app/templates')
redis = Redis(host='redis', port=6379)


def get_csv():
    path = './app/static/labels.csv'
    df = pd.read_csv(path)

    return df


@app.route('/')
def index():
    count = redis.incr('hits')
    template = 'home.html'
    return render_template(template, object=count)


@app.route('/tables')
def show_table():
    template = 'csvtable.html'
    df = get_csv()
    return render_template(template, object_list=df.to_html())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)