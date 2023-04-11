#!/usr/bin/env python3
"""
script provides stats on nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    function provides stats on ngix logs stored in the db
    """
    total_logs = mongo_collection.count_documents({})
    print('{} logs'.format(total_logs))
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        documents = mongo_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, documents))

    status = mongo_collection.count_documents({'method': 'GET',
                                               'path': '/status'})
    print("{} status check".format(status))


if __name__ == '__main__':
    with MongoClient() as client:
        db = client.logs.nginx
        log_stats(db)
