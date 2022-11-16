from flask import jsonify
from flask.views import MethodView

from querycontroller.query7 import query7


class q7api(MethodView):
    def __init__(self):
        self.q7 = query7()

    def get(self):
        result = self.q7.execute()
        # print(jsonify(result))
        return jsonify(result)