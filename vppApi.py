from flask import Flask, request
from pymongo import mongo_client
from bson.json_util import dumps

app = Flask(__name__)

@app.route('/users')
def get_users():
    config_mongo = configure_and_connect('users')
    users_result = query_users(config_mongo)
    config_mongo['client'].close()
    return dumps(users_result)

def query_users(config_mongo):
    users_result = []
    if config_mongo['collection'].count() > 0:
        cursor = config_mongo['collection'].find()
        for doc in cursor:
            users_result.append(doc)
    return users_result

@app.route('/user', methods=['POST'])
def add_user():
    user_data = request.json
    config_mongo = configure_and_connect('users')
    config_mongo['collection'].insert(user_data)
    config_mongo['client'].close()
    return dumps(user_data)

def configure_and_connect(collection_name):
    client = mongo_client.MongoClient('mongodb://ds031651.mongolab.com:31651')
    database = client['vppdev']
    database.authenticate('vppdev', 'vpp2015', mechanism='SCRAM-SHA-1')
    collection = database[collection_name]
    return {'client': client, 'collection': collection}

