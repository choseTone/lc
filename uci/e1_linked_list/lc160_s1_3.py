__author__ = 'wangqc'

# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/249917/Python-Two-Pointers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a