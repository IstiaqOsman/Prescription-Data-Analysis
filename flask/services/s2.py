from controller.c2 import Query2 

from flask import jsonify
from flask.views import MethodView
class Query2API(MethodView):
    def __init__(self):
        self.q2 = Query2()
    def get(self):
        result = self.q2.execute()
        return jsonify(result)