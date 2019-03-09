__author__ = 'wangqc'

'''
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        dummy = pre = ListNode(0)
        pre.next = head
        for _ in range(m-1):
            pre = pre.next
        cur, reverse = pre.next, None
        for _ in range(n-m+1):
            tmp, cur.next = cur.next, reverse
            reverse, cur = cur, tmp
        pre.next.next, pre.next = cur, reverse     # pre.next is the start node of the reversed interval
        return dummy.next

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
    ans = sol.reverseBetween(list2node([1, 2, 3, 4, 5]), 2, 4)
    print('ans: %s\ntime: %.3fms' % (node2list(ans), ((time() - t)) * 1000))
