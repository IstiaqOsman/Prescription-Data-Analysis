from flask import jsonify, request, Flask
from flask_cors import CORS

from router import query_api

app = Flask(__name__)
CORS(app)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'msg': 'Welcome Interns'})


@app.route('/hello/input', methods=['POST'])
def hello_input():
    data_dict = {}
    data_dict['name'] = request.json['name']
    data_dict['age'] = request.json['age']

    return jsonify({
        'NAME': data_dict['name'],
        'AGE': data_dict['age']
    })


app.register_blueprint(query_api, url_prefix='/project_api/')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
