#!/usr/bin/env python3

"""
text file that lists all documents in a collection:
returns an empty list if no document in the collection
"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """returns a list of documents in a collection"""
    documents = mongo_collection.find()
    return documents
