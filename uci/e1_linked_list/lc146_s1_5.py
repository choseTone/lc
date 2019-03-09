__author__ = 'wangqc'

'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity? Y

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

# https://leetcode.com/problems/lru-cache/discuss/251981/Java-Linked-List-%2B-Hashmap

'''
As per O(1) time complexity request, we could build a regular get and put based on a hashmap. 
When count of cache's nodes overflows cache's capacity, we need to evict one node based on LRU principle. 
We could use a double linked list to execute it so that all executions finish in O(1).

The base function is add which inserts a node at the head of the linked list. There are two occasions using add.
First, we put a brand new node to the cache. So we need to add it to the hashmap and increment the count of nodes. 
In this case, a key is passed to the function.
Second, we used a existed node so we need to update its postion in the linked list. 
I used another helper function update here to make code cleaner. 
In update, I remove the node from the linked list first then add it to the head so it becomes the most recently used node. 
In such case, there is no need to update hashmap and count. No key is passed to the function.

Besides, a new value is assigned to a existed node, we need to pass a value to update and update the value of hashmap[key] 
and move node to the head of linked list.
'''


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