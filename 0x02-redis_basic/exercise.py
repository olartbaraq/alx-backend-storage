#!/usr/bin/env python3
"""
text file to write strings into Redis,
create clss and instantiate, add methods
"""

from functools import wraps
from typing import Any, Union, Callable, Optional
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorator for counting how many times a function
    has been called """
    key = method.__qualname__

    @wraps(method)
    def raise_count(self, *args, **kwargs):
        """increase the count of when key is called"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return raise_count


def call_history(method: Callable) -> Callable:
    """Decorator for storing the history of inputs
    and outputs for a particular function"""
    @wraps(method)
    def wrap_history(self, *args, **kwargs):
        """Wrapper for decorator functionality """
        inputlist = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", inputlist)
        outputlist = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", outputlist)
        return outputlist
    return wrap_history


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

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method to return a string from any argument"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """method to convert back to the desired format"""
        corres_value = self._redis.get(key)
        if fn:
            corres_value = fn(corres_value)
        return corres_value

    def get_str(self, key: str) -> str:
        """parametrize the string format of a value"""
        return self.get(key, str)

    def get_int(self, key: int) -> int:
        """parametrize the integer format of a value"""
        return self.get(key, int)
