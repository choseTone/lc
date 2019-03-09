__author__ = 'wangqc'

'''
460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: 
get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, 
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when 
there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LFUCache cache = new LFUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

import collections

class LFUCache:

    freq = -1

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = {}
        self.lists = collections.defaultdict(collections.OrderedDict)

    def get(self, key):
        if key not in self.count: return -1
        count = self.count[key]
        self.count[key] += 1
        val = self.lists[count].pop(key)
        if count == self.freq and not self.lists[count]:
            self.freq += 1
        self.lists[count + 1][key] = val
        return val

    def put(self, key, value):
        if not self.capacity: return
        if key in self.count:
            self.lists[self.count[key]][key] = value
            self.get(key)
            return
        if len(self.count) == self.capacity:
            evict, _ = self.lists[self.freq].popitem(last=False)
            self.count.pop(evict)
        self.count[key] = self.freq = 1
        self.lists[1][key] = value


if __name__ == '__main__':

    obj = LFUCache(2)
    print(obj.put(1, 1))
    print(obj.put(2, 2))
    print(obj.get(1))
    print(obj.put(3, 3))
    print(obj.get(2))
    print(obj.get(3))
    print(obj.put(4, 4))
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))


