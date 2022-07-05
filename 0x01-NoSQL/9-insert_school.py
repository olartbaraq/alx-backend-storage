#!/usr/bin/env python3
"""
a python script that inserts a new document in a collection
based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """returns the object id of the document"""
    insert_items = {}
    for key, value in kwargs.items():
        insert_items[key] = value
    insert_result = mongo_collection.insert_one(insert_items)
    return insert_result.inserted_id
