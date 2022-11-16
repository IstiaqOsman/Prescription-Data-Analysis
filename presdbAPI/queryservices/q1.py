from flask import jsonify
from flask.views import MethodView

from querycontroller.query1 import query1


class q1api(MethodView):
    def __init__(self):
        self.q1 = query1()

    def get(self):
        result = self.q1.execute()
        # print(jsonify(result))
        return jsonify(result)