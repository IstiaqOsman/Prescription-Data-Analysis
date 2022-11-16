from flask import jsonify
from flask.views import MethodView

from querycontroller.query3 import query3


class q3api(MethodView):
    def __init__(self):
        self.q3 = query3()

    def get(self):
        result = self.q3.execute()
        # print(jsonify(result))
        return jsonify(result)