from flask import jsonify
from flask.views import MethodView

from querycontroller.query2 import query2


class q2api(MethodView):
    def __init__(self):
        self.q2 = query2()

    def get(self):
        result = self.q2.execute()
        # print(jsonify(result))
        return jsonify(result)