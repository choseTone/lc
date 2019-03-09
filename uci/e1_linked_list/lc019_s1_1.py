__author__ = 'wangqc'

'''
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass? Y
'''

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/247310/python-one-pass

'''
Suppose the length of linked list is L, the distance between the node to delete and the tail is |node-tail| = N.
Then |node-head| = L-N. So we can use two pointers here to get that L-N.

Pointer a first walks N units and there are L-N units left that a can walk. Then we have b start walking from the head
and a keep walking simultaneously.
After L-N rounds, a will reach the tail and b has walked L-N from the head, with a distance N away from the tail.
So when a reaches the tail, we know the node that b is pointing at is what to delete.

In case the head node is what to delete, we can create a dummy head whose next node is the head.
Then we have both a and b point at the dummy and eventually return dummy.next.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        a = b = dummy = ListNode(0)
        dummy.next = head
        for _ in range(n):
            a = a.next
        while a.next:
            a, b = a.next, b.next
        b.next = b.next.next
        return dummy.next

'''
It's a one pass O(n) time O(1) space solution.
'''