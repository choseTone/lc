__author__ = 'wangqc'

# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoListsIter(l1, l2):
    merge = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            merge.next, l1 = l1, l1.next
        else:
            merge.next, l2 = l2, l2.next
        merge = merge.next
    merge.next = l1 or l2
    return dummy.next

def mergeTwoListsRecu(l1, l2):
    if not (l1 and l2):
        return l1 or l2
    elif l1.val < l2.val:
        l1.next = mergeTwoListsRecu(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoListsRecu(l1, l2.next)
        return l2