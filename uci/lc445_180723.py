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


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        s1, s2 = self.read(l1), self.read(l2)
        sum_val, ans = 0, ListNode(0)
        while s1 or s2:
            if s1: sum_val += s1.pop()
            if s2: sum_val += s2.pop()
            ans.val = sum_val % 10
            sum_val //= 10
            prev_node = ListNode(sum_val)
            prev_node.next = ans
            ans = prev_node
        return ans if ans.val else ans.next

    def read(self, l):
        s = []
        while l:
            s.append(l.val)
            l = l.next
        return s


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
    l1, l2 = list2node([7,2,4,3]), list2node([5,6,4])
    ans = sol.addTwoNumbers(l1, l2)
    print('ans: %s\ntime: %.3fms' % (node2list(ans), ((time() - t)) * 1000))
