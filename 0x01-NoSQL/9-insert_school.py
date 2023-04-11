#!/usr/bin/env python3
"""
insert a document
"""


def insert_school(mongo_collection, **kwargs):
    """
    function takes a collecton and arguments
    using "insert_one" to insert one document to the collectoin
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
