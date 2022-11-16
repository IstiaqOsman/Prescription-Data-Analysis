from flask import jsonify
from flask.views import MethodView

from querycontroller.query6 import query6


class q6api(MethodView):
    def __init__(self):
        self.q6 = query6()

    def get(self):
        result = self.q6.execute()
        # print(jsonify(result))
        return jsonify(result)