from flask import Flask
from flask_restful import Api

from config import API_VESION


app = Flask(__name__)
app.config.from_object('config.CONFIG')

api = Api(app)


def add_api(handler, url):
    api.add_resource(handler, '/api/' + API_VESION + '/' + url)

from app import handlers
add_api(handlers.TestHandler, 'test')
