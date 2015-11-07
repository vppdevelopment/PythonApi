from flask import Flask, jsonify, request
from common.messages import User
from pymongo import mongo_client

app = Flask(__name__)

_users = []

@app.route('/users')
def get_users():
    configMongo = configure_and_connect('users')
    if configMongo['collection'].count() > 0:
        qusers = configMongo['collection'].find()
    else:
        qusers = {}
    print(qusers)
    return jsonify(users = qusers)

@app.route('/user', methods=['POST'])
def add_user():
    json = request.json
    _users.append(json)
    return jsonify(json)

def configure_and_connect(collectionName):
    client = mongo_client.MongoClient('mongodb://ds031651.mongolab.com:31651')
    database = client['vppdev']
    database.authenticate('vppdev', 'vpp2015', mechanism='SCRAM-SHA-1')
    collection = database[collectionName]
    return { 'client': client, 'collection': collection }

