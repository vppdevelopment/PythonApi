__author__ = 'maxne'

import unittest
from pymongo import mongo_client

class MongoDataManipulationTest(unittest.TestCase):

    def test_connection_and_basic_query(self):
       client = mongo_client.MongoClient('mongodb://ds031651.mongolab.com:31651')
       database = client['vppdev']
       database.authenticate('vppdev', 'vpp2015', mechanism='SCRAM-SHA-1')
       collection = database['registro']
       document = collection.find_one()
       client.close()
       print(document)

    def test_insertion(self):
        client = mongo_client.MongoClient('mongodb://ds031651.mongolab.com:31651')
        database = client['vppdev']
        database.authenticate('vppdev', 'vpp2015', mechanism='SCRAM-SHA-1')
        collection = database['registro']
        newDocument = {'Port': 25, 'Server': 'localhost', 'api':'custom' }
        collection.insert(newDocument)

if __name__ == '__main__':
    unittest.main()
