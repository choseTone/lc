__author__ = 'wangqc'


# https://leetcode.com/problems/design-hashmap/

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None

N = 10000

class MyHashMap:

    def __init__(self):
        self.N = N
        self.H = [Node(None, None) for _ in range(N)]

    def put(self, key, val):
        node = self.loc(key)
        while node.next and node.next.key != key:
            node = node.next
        if node.next:
            node.next.val = val
        else:
            node.next = Node(key, val)

    def get(self, key):
        node = self.loc(key)
        while node and node.key != key:
            node = node.next
        return node.val if node else -1

    def remove(self, key):
        node = self.loc(key)
        while node.next and node.next.key != key:
            node = node.next
        if node.next:
            node.next = node.next.next

    def loc(self, key):
        return self.H[key % self.N]


if __name__ == '__main__':
    obj = MyHashMap()
    print(obj.put(1, 1))
    print(obj.put(2, 2))
    print(obj.get(1))
    print(obj.get(3))
    print(obj.put(2, 1))
    print(obj.get(2))
    print(obj.remove(2))
    print(obj.get(2))
