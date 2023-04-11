#!/usr/bin/env python3
"""
script returns the list of school with specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    function takes 2 argument: 1- db_collection, 2-string to locate
    """
    return mongo_collection.find({'topics': {'$in': [topic]}})
