__author__ = 'wangqc'

'''
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. 
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/249917/Python-Two-Pointers

'''
Suppose there are two linked lists A and B with an intersection I starting at node X. The length of interaction is L,
A's length is L1+L and B's is L2+L.
And we have two pointers, a and b, walk through A and B in such way that a first walks through A then switch to B
while b first walks through B then switch to A.

In such manner, when a and b have walked a distance of L1+L2+L, a has walked through |A|+|B-I| (L1+L+L2)
and reaches X while b has walked through |B|+|A-I| (L2+L+L1) and reaches X as well.
Therefore, both a and b points to the start node of interaction when they first meet each other (a == b).

Meanwhile, if A and B has no intersection (L = 0), a reaches the end of B and b reaches the end of A.
Both of them point to None (a==b==None), which is also what to return. So we can combine two cases in such way:
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

'''
The time complexity is O(L1+L2+L) and space complexity if O(1)
'''