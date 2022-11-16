from flask import jsonify
from flask.views import MethodView

from querycontroller.query10 import query10



class q10api(MethodView):
    def __init__(self):
        self.q10 = query10()

    def get(self):
        result = self.q10.execute()
        # print(jsonify(result))
        return jsonify(result)