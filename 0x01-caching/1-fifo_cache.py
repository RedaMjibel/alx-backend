#!/usr/bin/python3
"""
FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system """
    def __init__(self):
        """init"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item value """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.cache_order.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
