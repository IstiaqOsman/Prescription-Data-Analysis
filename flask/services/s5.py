from controller.c5 import Query5 

from flask import jsonify
from flask.views import MethodView
class Query5API(MethodView):
    def __init__(self):
        self.q5 = Query5()
    def get(self):
        result = self.q5.execute()
        return jsonify(result)