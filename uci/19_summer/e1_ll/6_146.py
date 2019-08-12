__author__ = 'wangqc'


# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.keys = dict()
        self.head = self.tail = Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.sz = 0

    def insert(self, node, key=None):
        node.prev, node.next = self.head, self.head.next
        self.head.next = node.next.prev = node
        if key:
            self.keys[key] = node
            self.sz += 1

    def update(self, node, val=None):
        node.prev.next, node.next.prev = node.next, node.prev
        self.insert(node)
        if val:
            node.val = val

    def evict(self):
        del self.keys[self.tail.prev.key]
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.sz -= 1

    def get(self, key):
        if key not in self.keys:
            return -1
        self.update(self.keys[key])
        return self.keys[key].val

    def put(self, key, val):
        if key not in self.keys:
            self.insert(Node(key, val), key)
            if self.sz > self.cap:
                self.evict()
        else:
            self.update(self.keys[key], val)


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
