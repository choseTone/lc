__author__ = 'wangqc'

'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# https://leetcode.com/problems/merge-k-sorted-lists/discuss/252016/Python-Divide-and-Conquer

'''
To merge k sorted lists, we can implement divide & conquer and achieved a O(nlogk) time complexity.
Since all lists are sorted, we could easily merge two lists to one sorted lists as #148. 
Then we keep merging two larger merged lists in next iteration.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        k, d = len(lists), 1
        while d < k:
            for i in range(0, k - d, d * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + d])
            d *= 2
        return lists and lists[0]  # if lists is empty, return the empty list

    def merge2Lists(self, l1, l2):
        head = node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val: node.next, l1 = l1, l1.next
            else: node.next, l2 = l2, l2.next
            node = node.next
        node.next = l1 or l2
        return head.next

'''
For each iteration, we have to traverse all nodes in the lists so it costs O(n). And by divide & conquer, 
it takes logk iterations at all (k as number of lists). So total time complexity is nlogk
And we applied the in-place merge so space complexity is O(1).
'''