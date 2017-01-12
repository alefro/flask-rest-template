import os
import multiprocessing
import logging


HOST = 'localhost'
PORT = 5000
API_VESION = 'v1'


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

LOG_LEVEL = logging.DEBUG

GUNICORN_WORKERS = 1 + 2 * multiprocessing.cpu_count()


class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProdConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

CONFIG = DevConfig
