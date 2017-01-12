import datetime
from enum import Enum
from flask_restful import Resource
from flask_responses import json_response


class BaseHandler(Resource):
    def __init__(self):
        self.date_time_now = datetime.datetime.utcnow()

    def success_response(self, data):
        return json_response(data, status_code=RESPONSE_CODE.success)

    def bad_response(self, message):
        return json_response({"message": message}, status_code=RESPONSE_CODE.bad_request)


class RESPONSE_CODE(Enum):
    success = 200
    bad_request = 400
