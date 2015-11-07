__author__ = 'maxneo'

import unittest
from pymongo import mongo_client
from bson.json_util import dumps

class MongoDataManipulationTest(unittest.TestCase):

    def test_connection_and_basic_query(self):
       client = mongo_client.MongoClient('mongodb://ds031651.mongolab.com:31651')
       database = client['vppdev']
       database.authenticate('vppdev', 'vpp2015', mechanism='SCRAM-SHA-1')
       collection = database['registro']
       document = collection.find_one()
       client.close()
       print(type(document))

    def test_insertion(self):
        client = mongo_client.MongoClient('mongodb://ds031651.mongolab.com:31651')
        database = client['vppdev']
        database.authenticate('vppdev', 'vpp2015', mechanism='SCRAM-SHA-1')
        collection = database['registro']
        new_document = {u'Port': 25, u'Server': u'localhost', u'api':u'custom' }
        print(type(new_document))
        collection.insert(new_document)
        print(dumps(new_document))

if __name__ == '__main__':
    unittest.main()
