#!/usr/bin/env python3
"""
function to list document in a collection
"""


def list_all(mongo_collection):
    """
    this method lists all document in a collection
    """
    return mongo_collection.find()
