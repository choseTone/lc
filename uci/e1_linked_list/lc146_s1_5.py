__author__ = 'wangqc'

# https://leetcode.com/problems/lru-cache/discuss/251981/Java-Linked-List-%2B-Hashmap

class Node:
    def __init__(self, k=None, v=None):
        self.key = k
        self.val = v
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.keys = dict()
        self.h = self.t = Node()
        self.h.next, self.t.prev = self.t, self.h
        self.sz = 0

    def add(self, node, update=False):
        node.prev, node.next = self.h, self.h.next
        self.h.next = node.next.prev = node
        if not update: self.sz += 1

    def update(self, node, val=None):
        if val: node.val = val
        node.prev.next, node.next.prev = node.next, node.prev
        self.add(node, True)

    def evict(self):
        del self.keys[self.t.prev.key]
        self.t.prev = self.t.prev.prev
        self.t.prev.next = self.t

    def get(self, key):
        if key not in self.keys: return -1
        self.update(self.keys[key])
        return self.keys[key].val

    def put(self, key, value):
        if key not in self.keys:
            node = Node(key, value)
            self.keys[key] = node
            self.add(node)
            if self.sz > self.cap: self.evict()
        else:
            self.update(self.keys[key], value)