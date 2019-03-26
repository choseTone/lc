__author__ = 'wangqc'


# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/250983/Python-One-Pass

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    prev = dummy = ListNode(0)
    prev.next = head
    while head and head.next:
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head = head.next
        else:
            prev, head = prev.next, head.next
    return dummy.next