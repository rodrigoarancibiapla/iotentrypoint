import os
from flask import Flask, request, current_app

appFlask = Flask(__name__)

appFlask.config['PUBSUB_TOPIC'] = os.environ['PUBSUB_TOPIC']
appFlask.config['PROJECT'] = os.environ['GOOGLE_CLOUD_PROJECT']


from app.views import default


