from flask import json, request, Blueprint

test_api = Blueprint('test_api', __name__, template_folder='template')

@test_api.route('/test_api_get', methods=['GET'])
def test_api_get():
    if request.method == 'GET':
        return json.jsonify({
            'data': 'test_api_get'
        })

@test_api.route('/test_api_post', methods=['POST'])
def test_api_post():
    if request.method == 'POST':
        data = request.args.get('data')
        if data:
            if data != "":
                return json.jsonify({
                    'data': data
                })
            else:
                return json.jsonify({
                    'data': 'data is empty'
                })
        