__author__ = 'wangqc'

# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/251747/Python-One-Pass-in-Place

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    dummy = curr = ListNode(0)
    curr.next = head
    while True:
        tail = curr.next
        for _ in range(k):
            if not tail: return dummy.next
            tail = tail.next
        node, rev = curr.next, None
        for _ in range(k):
            node.next, node, rev = rev, node.next, node
        curr.next.next, curr.next, curr = node, rev, curr.next
