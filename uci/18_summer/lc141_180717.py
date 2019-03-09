__author__ = 'wangqc'

'''
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast: return True
        return False


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n1
    # n1.next, n2.next, n3.next, n4.next = n2, n3, n4, ListNode(5)
    ans = sol.hasCycle(n1)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
