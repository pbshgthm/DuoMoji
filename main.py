from flask import Flask, render_template
import atexit
from apscheduler.scheduler import Scheduler
from flask_sse import sse
import time,json
import stream



#run redis with
#redis-server /usr/local/etc/redis.conf

app = Flask(__name__)



cron = Scheduler(daemon=True)
cron.start()

@cron.interval_schedule(seconds=0.1)
def publish_hello():
    with app.app_context():
        buf=stream.buffer
        if not len(buf)==0:
            #print(buf)
            sse.publish({"message": buf,"timestamp":time.time()}, type='nodelink')
            sse.publish({})
            stream.buffer=[]

atexit.register(lambda: cron.shutdown(wait=False))


app.config["REDIS_URL"] = "redis://h:pb62d2c4f8006a7aaa8d011c6b07d42daab2f5a2a8d333911b5b803b90c9be195@ec2-3-208-45-52.compute-1.amazonaws.com:11079"
app.register_blueprint(sse, url_prefix='/stream')
stream.trackStream()

@app.route('/')
def index():
    data=json.loads(open('data.json').read())
    return render_template("dee3.html",data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)



#gunicorn main:app --worker-class gevent --bind 127.0.0.1:8000
