__author__ = 'wangqc'

# https://leetcode.com/problems/sort-list/discuss/250886/Python-Merge-Sort-O(nlogn)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def sortList(head):
    if not (head and head.next): return head
    mid, tail = head, head.next
    while tail and tail.next:
        mid, tail = mid.next, tail.next.next
    mid.next, mid = None, mid.next
    return merge(sortList(head), sortList(mid))

def merge(l1, l2):
    head = node = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val: node.next, l1 = l1, l1.next
        else: node.next, l2 = l2, l2.next
        node = node.next
    node.next = l1 or l2
    return head.next