from flask_restful import Resource


class TestHandler(Resource):
    def get(self):
        return "Success!"
