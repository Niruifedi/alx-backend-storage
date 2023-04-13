#!/usr/bin/env python3

import redis
from typing import Union
from uuid import uuid4

class Cache():
    
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        random = uuid4()
        rand = str(random)
        self._redis.set(rand, data)
        return rand
