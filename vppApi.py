from flask import Flask, jsonify
from common.messages import User

app = Flask(__name__)

@app.route('/users')
def getUsers():
    user = User()
    user.userName = 'maxneo'
    user.email = 'max@gmail.com'

    return jsonify(user.__dict__)