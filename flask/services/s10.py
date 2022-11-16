from controller.c10 import Query10 

from flask import jsonify
from flask.views import MethodView
class Query10API(MethodView):
    def __init__(self):
        self.q10 = Query10()
    def get(self):
        result = self.q10.execute()
        return jsonify(result)