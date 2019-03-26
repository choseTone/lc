__author__ = 'wangqc'

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/247310/python-one-pass

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    a = b = dummy = ListNode(0)
    dummy.next = head
    for _ in range(n):
        a = a.next
    while a.next:
        a, b = a.next, b.next
    b.next = b.next.next
    return dummy.next