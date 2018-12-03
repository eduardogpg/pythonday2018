from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import url_for
from flask import request

PORT = 8000
DEBUG = True
HOST = '0.0.0.0'

app = Flask(__name__)

users = [
    {
        'id' : 1,
        'username' : 'Python'
    }
]

def find_user(user_id=0):
    elements = [ user for user in users if user['id'] == user_id ]
    if len(elements) > 0:
        return elements[0]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.route('/codigo/api/v1.0/users/', methods=['GET'])
def get_courses():
    return jsonify({'users': users })

@app.route('/codigo/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    if user is not None:
        return jsonify({'user': user})

    abort(404)

@app.route('/codigo/api/v1.0/users/', methods=['POST'])
def create_user():
    print(request.json)

    if not request.json or not 'username' in request.json:
        abort(400)

    user = {
        'id': users[-1]['id'] + 1,
        'username': request.json['username'],
    }

    users.append(user)
    return jsonify( { 'user': user}), 201

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG, host=HOST)
