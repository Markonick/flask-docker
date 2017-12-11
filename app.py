from flask import Flask
from flask import render_template, redirect, url_for, request
from werkzeug import secure_filename
from redis import Redis
import pandas as pd


app = Flask(__name__, template_folder='app/templates')
redis = Redis(host='redis', port=6379)

def get_csv():
    path = './app/static/labels.csv'
    df = pd.read_csv(path)
    return df


@app.route('/')
@app.route('/home')
def index():
    count = redis.incr('hits')
    template = 'home.html'
    return render_template(template, title = "Home", count=count)


@app.route('/table')
def show_table():
    template = 'csvtable.html'
    df = get_csv()
    return render_template(template, object_list=df.to_html())


@app.route('/upload')
def upload():
    template = 'upload.html'
    return render_template(template)


@app.route('/uploader')
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


@app.route('/analysis_results')
def analysis_results():
    count = redis.incr('hits')
    template = 'analysis_results.html'
    return render_template(template, title = "Analysis Results", count=count)


@app.route('/contact')
def contact():
    count = redis.incr('hits')
    template = 'contact.html'
    return render_template(template, title = "Contacts", count=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)