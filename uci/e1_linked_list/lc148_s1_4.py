__author__ = 'wangqc'

'''
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# https://leetcode.com/problems/sort-list/discuss/250886/Python-Merge-Sort-O(nlogn)

'''
First we break the input linked list into two equal-size linked list from middle node (using slow and fast pointers,
when we get to the middle node, we save middle.next as a new linked list and set original middle.next as None).
Then like merge sort, we keep breaking linked list into two halves by recursive call.
After that, we merge two sorted linked list (at the bottom, there is only one node in each linked list so it's sorted)
into sorted one linked list by merge() in each recursion. merge just keep adding smaller node from l1 and l2
until they are empty.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        if not (head and head.next): return head
        mid, tail = head, head.next
        while tail and tail.next:
            mid, tail = mid.next, tail.next.next
        mid.next, mid = None, mid.next
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, l1, l2):
        head = node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val: node.next, l1 = l1, l1.next
            else: node.next, l2 = l2, l2.next
            node = node.next
        node.next = l1 or l2
        return head.next

'''
Using merge sort, the time complexity is O(nlognN) and space complexity is O(1). 
No extra space is used since we are just updating the existed pointers.
'''