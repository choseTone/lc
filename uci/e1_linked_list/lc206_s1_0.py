__author__ = 'wangqc'

'''
206. Reverse Linked List

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# https://leetcode.com/problems/reverse-linked-list/discuss/246827/python-iterative-recursive

'''
To reverse a linked list, we actually reverse the direction of every next pointer.
For example, we reverse a linked list 1->2->3->4->5 by changing every -> to <- and get the result as 1<-2<-3<-4<-5.
And we need to return the pointer to 5 instead of to 1.
To solve it efficiently, we can do it in one loop iteration or recursion.

For iteration, we create a ListNode rev to keep track of what we have reversed otherwise we would lose it.
Then we iterate linked list and make head point to the current node. We change a -> to <- by calling head.next = rev,
update rev by calling rev = head, move to next node by calling head = head.next. And we should do these three moves concurrently.
For example, 1->2->3, 1 is current node head, what we have reversed rev is None, 2 is head.next.
Calling head.next = rev leads to None<-1. Calling head = head.next concurrently to make head pointing to 2->3.
Updating rev as 1->None. And in next iteration, we will change 2->3 to 1<-2 and keep changing -> to <- so on so forth.


For recursion, the bottom layer is the end of the origin linked list so we just return it. For the outer layer, 
for example, 4->5, we change -> to <- by calling head.next.next = head where head points at 4 and head.next points at 5. 
node, which is self.reverseList(head.next) also points at 5 or 5->4, is what we need to return in this layer. 
So when we keep returning to the outer layer, reversed linked list keep growing (a -> b becomes a <- b as head.next.next = head)
Another example, in some recursion, you have linked list 1->2->3->null, reversed linked list 5->4->3->null. 
head points at 2, head.next points at 3, 5->4->3->null is what you have reversed and stored in node=reversedList(head.next). 
Now you need to place 2 to the end of 5->4->3. So you call head.next.next = head or 3.next = 2, and head.next = null or 2.next = null. 
Then you have original linked list 1->2->null, and reversed linked list (head node 5 stored in node) 5->4->3->2->null. 
Then you return these to outer recursion.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseListIter(self, head):
        rev = None
        while head:
            head.next, rev, head = rev, head, head.next
        return rev

    def reverseListRecu(self, head):
        if not head or not head.next: return head
        node, head.next.next, head.next = self.reverseListRecu(head.next), head, None
        return node

'''
One thing should be notice that we should always be fully aware of what a variable points at. The rev and reverseList_Recu(node) 
point at the head of the reversed linked list while the current node head that we are visiting in origin linked list point 
at the tail of the reversed linked list.
Both methods take a liner scan without extra space. So time complexity is O(n) and space is O(1).
'''