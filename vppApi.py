from flask import Flask, jsonify, request
from common.messages import User

app = Flask(__name__)

_users = []

@app.route('/users')
def getUsers():
    user = User()
    user.userName = 'maxneo'
    user.email = 'max@gmail.com'
    _users.append(user.__dict__)

    return jsonify(users=_users)

@app.route('/user', methods=['POST'])
def addUser():
    json = request.json
    print(json)
    # Render template
    return jsonify(json)