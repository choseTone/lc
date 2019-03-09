__author__ = 'wangqc'

'''
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/250983/Python-One-Pass

'''
Since we need to remove all duplicated node, we need a node prev points to the node before the duplicated one.
Then we can link prev.next to the first node that's not duplicated or None if rest nodes are all duplicated.
For each loop iteration, if there is a duplication, we traverse the linked list till the first non-duplicated node
(via a inner while loop) and link it to prev.next. If there isn't a duplication, we could safely move prev to its next.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
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

'''
It's a one-pass in-place solution so time complexity is O(1) and space complexity is O(1).
'''