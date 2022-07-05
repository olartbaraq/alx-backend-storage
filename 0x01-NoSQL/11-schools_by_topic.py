#!/usr/bin/env python3

"""
script that returns the list of school having a specific topic
"""
from typing import List


def schools_by_topic(mongo_collection,
                     topic: str) -> List[str]:
    """
    returns the list of school having a specific topic
    """
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return schools
