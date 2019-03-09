__author__ = 'wangqc'

'''
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first 
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

'''
A typical add two number question solution is to add two number's digits from right to left.
We add one carry unit to the next digit if the current sum is larger than 10 and set sum mod 10 as new digit value.
We also need to handle the situation when two number have different length.
For two numbers with the form of single linked list, the key challenge is that we have to read number from left to right.
Thus, we can either store digit val to a stack or solve it in recursive way.

Stack
We store linked list's val to a stack and then pop a digit out (LIFO) for each addition so that we add digits from right to left. 
We also create a new linked list ans to store our addition result. We keep add new added digit (saved in head) to its front.
If one stack is empty, we add nothing from it. If both stacks are empty, we finish our addition. 
And last addition's carry is saved in sum_val and carried to the next addition.
The time complexity is O(n) and space complexity is O(n) since we create two stacks and one linked list.

Recursion
To solve it in a more 'linked list' way, we can do it via recursion. We get right digits addition result from recursion 
and carry out current digit addition. Then store the recursion result to current node's next pointer. 
We do it by passing l1.next and l2.next to our recursive function.
We need to handle length difference issue. So we make sure l1's length is no smaller than l2's length by variable switch trick. 
And we add l2's node.val and move to l2.next only when l1's length equals to l2's length. 
Since l1 is longer, we save our addition result in l1's node to save some space. 
If the final carry is larger than 0, we add one new node at the head.
The time complexity is O(n) and space complexity is O(1) since we carry out our addition by updating l1's value
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbersStack(self, l1, l2):
        s1, s2 = self.read(l1), self.read(l2)
        sum_val, ans = 0, ListNode(0)
        while s1 or s2:
            if s1: sum_val += s1.pop()
            if s2: sum_val += s2.pop()
            sum_val, ans.val = divmod(sum_val, 10)
            head = ListNode(sum_val)
            head.next, ans = ans, head
        return ans if ans.val else ans.next

    def read(self, l):
        s = []
        while l:
            s.append(l.val)
            l = l.next
        return s

    def addTwoNumbersRecur(self, l1, l2):
        len1, len2, carry = self.getLen(l1), self.getLen(l2), 0
        if len1 < len2: l1, len1, l2, len2 = l2, len2, l1, len1
        carry = self.recur(l1, len1, l2, len2)
        if carry:
            head, head.next = ListNode(carry), l1
            return head
        return l1

    def recur(self, l1, len1, l2, len2):
        if not (l1 or l2): return 0
        (len1, l2v, l2n) = (len1 - 1, 0, l2) if len1 > len2 else (len1, l2.val, l2.next)
        carry, l1v = self.recur(l1.next, len1, l2n, len2), l1.val
        l1.val = (l1v + l2v + carry) % 10
        return (l1v + l2v + carry) // 10

    def getLen(self, node):
        l = 0
        while node:
            node, l = node.next, l + 1
        return l


