from flask import Flask
from flask import render_template, redirect, url_for
from redis import Redis
import pandas as pd


app = Flask(__name__, template_folder='app/templates')
redis = Redis(host='redis', port=6379)

def get_csv():
    path = './app/static/labels.csv'
    df = pd.read_csv(path)
    return df


@app.route('/')
def home():
    count = redis.incr('hits')
    template = 'home.html'
    return render_template(template, title = "Home", count=count)


@app.route('/table')
def show_table():
    template = 'csvtable.html'
    df = get_csv()
    return render_template(template, object_list=df.to_html())


@app.route('/upload')
def upload_file():
    count = redis.incr('hits')
    template = 'upload.html'
    return render_template(template)


@app.route('/contact')
def contact():
    count = redis.incr('hits')
    template = 'contact.html'
    return render_template(template, title = "Contacts", count=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)