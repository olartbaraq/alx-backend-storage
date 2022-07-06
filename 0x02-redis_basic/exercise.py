#!/usr/bin/env python3
"""
text file to write strings into Redis,
create clss and instantiate, add methods
"""

from typing import Any, Union, Callable
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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method to return a string from any argument"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key, fn=None):
        """method to convert back to the desired format"""
        corres_value = self._redis.get(key)
        if fn:
            data = fn(corres_value)
        return data

    def get_str(self, key):
        """parametrize the string format of a value"""
        return self.get(key, str)

    def get_str(self, key):
        """parametrize the integer format of a value"""
        return self.get(key, int)
