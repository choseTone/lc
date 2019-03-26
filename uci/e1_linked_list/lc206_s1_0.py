__author__ = 'wangqc'

# https://leetcode.com/problems/reverse-linked-list/discuss/246827/python-iterative-recursive

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseListIter(head):
    rev = None
    while head:
        head.next, rev, head = rev, head, head.next
    return rev

def reverseListRecu(head):
    if not head or not head.next: return head
    node, head.next.next, head.next = reverseListRecu(head.next), head, None
    return node