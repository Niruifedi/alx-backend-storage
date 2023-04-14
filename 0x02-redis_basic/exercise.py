#!/usr/bin/env python3
"""
Writing String to Redis
"""
import redis
from typing import Union, Callable, Optional
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
    
    def get(self, key: str, fn: Optional[Callable] = None) ->\
        Union[str, bytes, int, float]:
        return fn(self._redis.get(key)) if fn else self._redis.get(key)
    
    def get_str(self, data: bytes) -> str:
        return data.decode('utf-8')
    
    def get_int(self, data: bytes) -> int:
        return int(data)

    
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d:d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value