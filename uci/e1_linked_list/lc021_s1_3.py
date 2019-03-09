__author__ = 'wangqc'

'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# https://leetcode.com/problems/merge-two-sorted-lists/

'''
Iterative way is kind of a two-pointers method. We create a pointer merge to merge two linked list and have two pointers l1, l2
walk through two linked list respectively. Each time we add 'smaller' node to the end of merge
and forward at the owner linked list of that 'smaller' node until one of the linked list is exhausted.
Then we add the rest of the other linked list to the end of merge since all nodes' values in that linked list are sorted and larger.

Recursion way is similar. Each time we pick out the smaller node, which should be at the front of the merged linked list, 
and grow it with the merging of rest of it and the other linked list by recursive calls.
The base of the recursion is one of the linked list if exhausted. And we return the other one entirely as explained in iterative way.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoListsIter(self, l1, l2):
        merge = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                merge.next, l1 = l1, l1.next
            else:
                merge.next, l2 = l2, l2.next
            merge = merge.next
        merge.next = l1 or l2
        return dummy.next

    def mergeTwoListsRecu(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2
        elif l1.val < l2.val:
            l1.next = self.mergeTwoListsRecu(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecu(l1, l2.next)
            return l2

'''
Both methods' time complexity are O(|l1|+|l2|) and space complexity is O(1) since we allocate no extra node but just update some pointers.
'''