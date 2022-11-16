import json
from flask import Flask
from flask_cors import CORS
from router import query_api1,query_api2,query_api3,query_api4,query_api5,query_api6,query_api7,query_api8,query_api9,query_api10

app = Flask(__name__)
CORS(app)

app.register_blueprint(query_api1, url_prefix = '/api/')
app.register_blueprint(query_api2, url_prefix = '/api/')
app.register_blueprint(query_api3, url_prefix = '/api/')
app.register_blueprint(query_api4, url_prefix = '/api/')
app.register_blueprint(query_api5, url_prefix = '/api/')
app.register_blueprint(query_api6, url_prefix = '/api/')
app.register_blueprint(query_api7, url_prefix = '/api/')
app.register_blueprint(query_api8, url_prefix = '/api/')
app.register_blueprint(query_api9, url_prefix = '/api/')
app.register_blueprint(query_api10, url_prefix = '/api/')

if __name__ == '__main__':
    app.run(host = "localhost", port  = 5000)   