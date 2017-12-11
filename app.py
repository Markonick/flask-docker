from flask import Flask
from flask import render_template
from redis import Redis
import pandas as pd


app = Flask(__name__, template_folder='app/templates')
redis = Redis(host='redis', port=6379)


def get_csv():
    path = './app/static/labels.csv'
    """csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)"""
    df = pd.read_csv(path)
    csv_obj = list(df)
    csv_list = list(csv_obj)

    return csv_list


@app.route('/')
def index():
    count = redis.incr('hits')
    return 'Hello Pappefi and Markonick! You guys have now been seen {} times.\n'.format(count)


@app.route('/results')
def csv_results():
    template = 'results.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)