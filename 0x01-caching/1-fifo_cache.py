#!/usr/bin/env python3
"""
second task
"""


from collections import OrderDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    this class inherints from BC and is a
    caching system
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderDict()

    def put(self, key, item):
        """
        asssign self.cache_data item value for the key
        """

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        return value of self.cace_data
        """

        return self.cache_data.get(key, None)
