#!/usr/bin/env python3

"""
script that changes all topics of a school document based on
the name
"""
from typing import Any, Dict, List
from pymongo import MongoClient


def update_topics(mongo_collection,
                  name: str,
                  topics: List[str]):
    """
    returns the object id of the document
    that wants to be changed based on
    the name argument
    """
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}

    mongo_collection.update_many(myquery, newvalues)
