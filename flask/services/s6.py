from controller.c6 import Query6 

from flask import jsonify
from flask.views import MethodView
class Query6API(MethodView):
    def __init__(self):
        self.q6 = Query6()
    def get(self):
        result = self.q6.execute()
        return jsonify(result)