__author__ = 'wangqc'

'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order 
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        ans, carry = ListNode(0), 0
        l3 = ans
        while l1 or l2:
            a, b = l1.val if l1 else 0, l2.val if l2 else 0
            carry, digit = divmod(a + b + carry, 10)
            l3.next = ListNode(digit)
            l3 = l3.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: l3.next = ListNode(carry)
        return ans.next


if __name__ == '__main__':
    from time import time

    def list2node(list):
        head = node = ListNode(0)
        for val in list:
            node.next = ListNode(val)
            node = node.next
        return head.next

    def node2list(node):
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans

    sol = Solution()
    t = time()
    ans = sol.addTwoNumbers(list2node([2, 4, 3]), list2node([5, 6, 4]))
    print('ans: %s\ntime: %.3fms' % (node2list(ans), ((time() - t)) * 1000))
