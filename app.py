from flask import Flask
from flask import render_template
from redis import Redis
import pandas as pd

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

def get_csv():
    csv_path = './static/labels.csv'
    data = pd.read_csv(csv_path)
    csv_list = list(data)
    return csv_list

@app.route('/')
def index():
    count = redis.incr('hits')
    return 'Hello Pappefi and Markonick! You guys have been seen {} times.\n'.format(count)

@app.route('/csvresults')
def csv_results():
    template = 'csvresults.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)