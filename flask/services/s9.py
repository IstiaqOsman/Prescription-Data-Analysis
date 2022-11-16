from controller.c9 import Query9 

from flask import jsonify
from flask.views import MethodView
class Query9API(MethodView):
    def __init__(self):
        self.q9 = Query9()
    def get(self):
        result = self.q9.execute()
        return jsonify(result)