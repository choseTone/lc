__author__ = 'wangqc'

'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: 
get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it 
should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    # update node's position to the tail of the linked list since it's recently used
    def _update(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self._add(node)

    # evict the least recently used node at the head of the linked list
    def _evict(self):
        del self.cache[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def _add(self, node):
        node.prev, node.next = self.tail.prev, self.tail
        node.prev.next = self.tail.prev = node

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update(node)
        else:
            if self.count >= self.capacity:
                self._evict()
            else:
                self.count += 1
            node = Node(key, value)
            self._add(node)
            self.cache[key] = node


if __name__ == '__main__':

    obj = LRUCache(2)
    print(obj.put(1, 1))
    print(obj.put(2, 2))
    print(obj.get(1))
    print(obj.put(3, 3))
    print(obj.get(2))
    print(obj.put(4, 4))
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))


