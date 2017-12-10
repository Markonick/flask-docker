from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    count = redis.incr('hits')
    return 'Hello Pappefi & Markonick! You guys have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="localhost", debug=True)