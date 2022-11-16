from controller.c7 import Query7 

from flask import jsonify
from flask.views import MethodView
class Query7API(MethodView):
    def __init__(self):
        self.q7 = Query7()
    def get(self):
        result = self.q7.execute()
        return jsonify(result)