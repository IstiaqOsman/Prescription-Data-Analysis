from flask import jsonify
from flask.views import MethodView

from querycontroller.query5 import query5


class q5api(MethodView):
    def __init__(self):
        self.q5 = query5()

    def get(self):
        result = self.q5.execute()
        # print(jsonify(result))
        return jsonify(result)