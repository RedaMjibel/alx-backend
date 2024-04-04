#!/usr/bin/python3
"""
LFU caching
"""

from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """init"""
        super().__init__()
        self.cache_frequency = defaultdict(int)

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_frequency[key] += 1
        elif len(self.cache_data) >= self.MAX_ITEMS:
            least_frequent_key = min(self.cache_frequency, key=self.cache_frequency.get)
            del self.cache_data[least_frequent_key]
            del self.cache_frequency[least_frequent_key]
            print("DISCARD:", least_frequent_key)

        self.cache_data[key] = item
        self.cache_frequency[key] += 1

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        self.cache_frequency[key] += 1

        return self.cache_data[key]
