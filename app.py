import redis
from flask import Flask

app = Flask(__name__)


r = redis.Redis(
        host='localhost',
        port=6379)
        # password='password')

r.set("count", "0")

@app.route('/')
def get_visits():
    count = int(r.get('count'))
    r.set("count", str(count+1))
    return "Number of visits: {}".format(count)

if __name__ == '__main__':
    app.run(
            host='0.0.0.0',
            port=5000,
            debug=False
    )
