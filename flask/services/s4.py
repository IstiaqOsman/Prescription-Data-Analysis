from controller.c4 import Query4 

from flask import jsonify
from flask.views import MethodView
class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()
    def get(self):
        result = self.q4.execute()
        return jsonify(result)