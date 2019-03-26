__author__ = 'wangqc'

# https://leetcode.com/problems/design-linked-list/discuss/251789/Python-Clean-Two-Ends-Iteration

class Node:

    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class MyLinkedList:

    def __init__(self):
        self.h = self.t = Node(-1)
        self.h.next, self.t.prev = self.h, self.t
        self.sz = 0

    def add(self, refer, node):
        node.prev, node.next = refer.prev, refer
        refer.prev = node.prev.next = node
        self.sz += 1

    def rm(self, node):
        node.next.prev, node.prev.next = node.prev, node.next
        self.sz -= 1

    def fwd(self, i, j, node):
        for _ in range(i, j): node = node.next
        return node

    def bck(self, j, i, node):
        for _ in range(i, j): node = node.prev
        return node

    def getNode(self, i):
        if 0 <= i < self.sz >> 1:
            return self.fwd(0, i, self.h.next)
        elif self.sz >> 1 <= i < self.sz:
            return self.bck(self.sz - 1, i, self.t.prev)

    def get(self, i):
        return self.getNode(i).val if 0 <= i < self.sz else -1

    def addAtHead(self, val):
        self.add(self.h.next, Node(val))

    def addAtTail(self, val):
        self.add(self.t, Node(val))

    def addAtIndex(self, i, val):
        if 0 <= i < self.sz:
            self.add(self.getNode(i), Node(val))
        elif i == self.sz:
            self.addAtTail(val)

    def deleteAtIndex(self, i):
        if 0 <= i < self.sz: self.rm(self.getNode(i))