from flask import jsonify
from flask.views import MethodView

from querycontroller.query9 import query9


class q9api(MethodView):
    def __init__(self):
        self.q9 = query9()

    def get(self):
        result = self.q9.execute()
        # print(jsonify(result))
        return jsonify(result)