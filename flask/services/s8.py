from controller.c8 import Query8 

from flask import jsonify
from flask.views import MethodView
class Query8API(MethodView):
    def __init__(self):
        self.q8 = Query8()
    def get(self):
        result = self.q8.execute()
        return jsonify(result)