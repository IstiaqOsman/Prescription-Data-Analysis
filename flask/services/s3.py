from controller.c3 import Query3 

from flask import jsonify
from flask.views import MethodView
class Query3API(MethodView):
    def __init__(self):
        self.q3 = Query3()
    def get(self):
        result = self.q3.execute()
        return jsonify(result)