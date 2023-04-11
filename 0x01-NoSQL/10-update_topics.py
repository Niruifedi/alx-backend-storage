#!/usr/bin/env python3
"""
script to update documents
"""


def update_topics(mongo_collection, name, topics):
    """
    function takes 3 argument: collection, string to update and value
    """
    return mongo_collection.update_many({'name': name},
                                        {'$set': {'topics': topics}})
