__author__ = 'wangqc'

# https://leetcode.com/problems/linked-list-cycle-ii/discuss/249727/Python-Two(Three)-Pointers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    a = b = c = head
    while a and a.next:
        a, b = a.next.next, b.next
        if a == b:
            while b != c:
                b, c = b.next, c.next
            return b
    return None
