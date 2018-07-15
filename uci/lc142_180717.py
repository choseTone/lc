__author__ = 'wangqc'

'''
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        entry = slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                while entry is not slow:
                    entry, slow = entry.next, slow.next
                return entry
        return None


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    # n1.next, n2.next, n3.next, n4.next = n2, n3, n4, ListNode(5)
    ans = sol.detectCycle(n1)
    print('ans: %s\ntime: %.3fms' % (ans and ans.val, ((time() - t)) * 1000))
