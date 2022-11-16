from controller.c1 import Query1 

from flask import jsonify
from flask.views import MethodView
class Query1API(MethodView):
    def __init__(self):
        self.q1 = Query1()
    def get(self):
        result = self.q1.execute()
        return jsonify(result)