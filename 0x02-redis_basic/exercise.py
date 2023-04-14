#!/usr/bin/env python3
"""
Writing String to Redis
"""
from functools import wraps
import redis
from typing import Union, Callable, Optional
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
    counts number of calls made to Cache
    """
    key = method.__qualname__

    @wraps(method)
    def count(self, *args, **kwargs):
        """
        decorator method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return count


class Cache():
    """
    class Cache
    """
    def __init__(self):
        """
        class constructor to instantiate redis connection
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method recieves an input data and stores it with a randomly generated
        uuid as key
        """
        random = uuid4()
        self._redis.set(str(random), data)
        return str(random)

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """
        retieves value from server, convert it to desired format
        """
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, data: bytes) -> str:
        """
        function recieves data as bytes and converts it to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        function recieves data as bytes and converts it to integer
        """
        return int(data)
