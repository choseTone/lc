__author__ = 'wangqc'

'''
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
'''


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

import collections

class Solution:
    def copyRandomList(self, head):
        copy = collections.defaultdict(lambda: RandomListNode(0))
        copy[None], dummy = None, head
        while head:
            copy[head].label = head.label
            copy[head].next = copy[head.next]
            copy[head].random = copy[head.random]
            head = head.next
        return copy[dummy]

