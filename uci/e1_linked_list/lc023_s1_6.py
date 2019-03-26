__author__ = 'wangqc'

# https://leetcode.com/problems/merge-k-sorted-lists/discuss/252016/Python-Divide-and-Conquer

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    k, d = len(lists), 1
    while d < k:
        for i in range(0, k - d, d * 2):
            lists[i] = merge2Lists(lists[i], lists[i + d])
        d *= 2
    return lists and lists[0]

def merge2Lists(l1, l2):
    head = node = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val: node.next, l1 = l1, l1.next
        else: node.next, l2 = l2, l2.next
        node = node.next
    node.next = l1 or l2
    return head.next