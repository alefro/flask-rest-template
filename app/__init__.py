from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from raven.contrib.flask import Sentry

from config import API_VESION


app = Flask(__name__)
app.config.from_object('config.CONFIG')

api = Api(app)
CORS(app, resources={"/api/" + API_VESION + "/*": {"origins": "*"}})
sentry = Sentry(app, dsn='http://')


def add_api(handler, url):
    api.add_resource(handler, '/api/' + API_VESION + '/' + url)

from app.handlers import test_handler
add_api(test_handler.TestHandler, 'test')
