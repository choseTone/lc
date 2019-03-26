__author__ = 'wangqc'

# https://leetcode.com/problems/middle-of-the-linked-list/discuss/249691/Python-Two-Pointers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head):
    a = b = head
    while b and b.next:
        a, b = a.next, b.next.next
    return a