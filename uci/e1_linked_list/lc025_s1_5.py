__author__ = 'wangqc'

'''
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not 
a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/251747/Python-One-Pass-in-Place

'''
It's like the updated version of #92, where we need to reverse a range of nodes in a given linked list.
In this question, we just do it in a k stride.
Each time we forward k steps in advance. If we reach the tail before the kth step, we just return the linked list
as per the request that the left-out list should remain as it is.
Then we reverse all the nodes within this k-steps range as #92.
As #206, we have two pointers node and rev pointing to current node and the head of reversed list.
We keep forwarding with node and adding node to the front of rev.
For example
1st iter: node 1->2->3->4->5  rev None
2nd iter: node 2->3->4->5     rev 1->None
3rd iter: node 3->4->5        rev 2->1->None
We need to reverse k nodes so we do such reversion for k times. We save the node before the reversed range as curr.
For example, after k-times reversion is finished,

Before reversion
curr 1->2->3->4->5.
After reversion (range: 2->3->4)
curr 1->2
rev  4->3->2->None
node 5
node points to the next node of reversed range(which is 5), we should set it as the next node of the tail node (which is 2)
of the reversed list. Tail node is the head node before the reversion and we haven't update curr yet, so it's curr.next.
So we set curr.next.next = node.
1->2->5
(notice 5 is now set next to 2 so rev becomes 4->3->2->5 as well)
And then we updated curr.next to the head of reversed list (rev) and concurrently move curr to curr.next(2).
So we will have list:
1->4->3->2->5
while curr now points to 2 as the node before the next reversed range. And we can move to next k-steps iteration.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = curr = ListNode(0)
        curr.next = head
        while True:
            tail = curr.next  # tail serves as a sentinel detecting the tail of the linked list
            for _ in range(k):  # detect before reverse, which will alter the list, so the left-over remain as it is
                if not tail: return dummy.next  # reach the tail and return
                tail = tail.next
            node, rev = curr.next, None
            for _ in range(k):
                node.next, node, rev = rev, node.next, node
            curr.next.next, curr.next, curr = node, rev, curr.next

    '''
    This is a one-pass(actually two passes as detect+reverse) in-place solution so it's O(2n) time complexity and O(1) space complexity.
    '''