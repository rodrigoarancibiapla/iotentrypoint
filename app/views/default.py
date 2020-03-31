import datetime
import json
import google.cloud.logging
client = google.cloud.logging.Client()
client.setup_logging()
import logging
import sys
from app import appFlask as myapp
from app import request, current_app
from app.models import pubsub

@myapp.route('/', methods=['POST'])
def index():
    
    data={}
    utc_datetime = datetime.datetime.utcnow()
    data['datetime'] = utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
    for arg in request.args:
        data[arg] = request.args.get(arg)
    try:
        logging.info("publishing: " + json.dumps(data))
        pubsub.publish(current_app.config['PROJECT'], current_app.config['PUBSUB_TOPIC'], json.dumps(data).encode('utf-8'))
        return 'OK', 200
    except:
        logging.error("Error publishing: " + str(sys.exc_info()[1]))
        return 'ERROR',500
