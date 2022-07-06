#!/usr/bin/env python3
"""
text file to write strings into Redis,
create clss and instantiate, add methods
"""

from typing import Any, Union
import uuid
import redis


class Cache():
    """
    Cache class to store Redis client instance
    """
    def __init__(self):
        """instantiation method to store Redis
        client varaibles
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """method to return a string from any argument"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
