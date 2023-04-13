#!/usr/bin/env python3
"""
Writing String to Redis
"""
import redis
from typing import Union
from uuid import uuid4


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method recieves an input data and stores it with a randomly generated
        uuid as key
        """
        random = uuid4()
        self._redis.set(str(random), data)
        return str(random)
