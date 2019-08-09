__author__ = 'wangqc'


# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


class MyLinkedList:

    def __init__(self):
        self.h = self.t = Node(-1)
        self.h.next, self.t.prev = self.t, self.h
        self.sz = 0

    def add(self, pos, node):
        node.prev, node.next = pos.prev, pos
        pos.prev = node.prev.next = node
        self.sz += 1

    def rm(self, node):
        node.next.prev, node.prev.next = node.prev, node.next
        self.sz -= 1

    def fwd(self, node, k):
        for _ in range(k):
            node = node.next
        return node

    def bck(self, node, k):
        for _ in range(k):
            node = node.prev
        return node

    def get_node(self, i):
        return self.fwd(self.h.next, i) if 0 <= i < self.sz>>1 \
            else self.bck(self.t.prev, self.sz-1-i)

    def get(self, index):
        return self.get_node(index).val if 0 <= index < self.sz else -1

    def addAtHead(self, val):
        self.add(self.h.next, Node(val))

    def addAtTail(self, val):
        self.add(self.t, Node(val))

    def addAtIndex(self, index, val):
        if 0 <= index < self.sz:
            self.add(self.get_node(index), Node(val))
        elif index == self.sz:
            self.addAtTail(val)
        elif index < 0:
            self.addAtHead(val)

    def deleteAtIndex(self, index):
        if 0 <= index < self.sz: self.rm(self.get_node(index))


if __name__ == '__main__':
    obj = MyLinkedList()
    print(obj.addAtHead(1))
    print(obj.addAtTail(3))
    print(obj.addAtIndex(1, 2))
    print(obj.get(1))
    print(obj.deleteAtIndex(1))
    print(obj.get(1))
