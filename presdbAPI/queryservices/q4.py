from flask import jsonify
from flask.views import MethodView
from querycontroller.query4 import query4


class q4api(MethodView):
    def __init__(self):
        self.q4 = query4()

    def get(self):
        result = self.q4.execute()
        # print(jsonify(result))
        return jsonify(result)