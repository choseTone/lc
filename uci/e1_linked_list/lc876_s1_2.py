__author__ = 'wangqc'

'''
876. Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list. 
If there are two middle nodes, return the second middle node.
 
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Note:
The number of nodes in the given list will be between 1 and 100.
'''

# https://leetcode.com/problems/middle-of-the-linked-list/discuss/249691/Python-Two-Pointers

'''
Suppose we have two pointers a and b and our linked list has a length of 2L. a's stride is 1 and b's stride is 2.
So when b reaches the tail, a moves a distance of L, where is the middle of the linked list.
The node a points to the middle node we need.

If linked list has 2L or 2L+1 nodes, we both need to return the (L+1)th node.

First, suppose linked list has 2L+1 nodes (L could be 0), we can start moving a and b from the 1st node.
Then after L iterations, b moves a distance of 2L and reaches the (2L+1)th node(last node) and we should stop loop.
And a moves a distance of L and stops at the (L+1)th node.

Second, suppose linked list has 2L nodes(L > 0), if we still start moving a and b from the 1st node, then after L-1 iterations,
b moves a distance of 2L-2 and reaches the (2L-1)th node and a stops at the Lth node.
Now b can still forward with a stride of 2 and points to the (2L+1)th node.next which is None and a stops at the (L+1)th node as required.

Thus, in both cases, we start moving a and b from the 1st node and stop loop when b(b=(2L+1)th node.next in case of 2L nodes)
or b.next(b=(2L+1)th node in case of (2L+1) nodes) is None. By then a will point to what we need.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        a = b = head
        while b and b.next:
            a, b = a.next, b.next.next
        return a

'''
And two pointers give us a O(n) time complexity and O(1) space complexity.
'''