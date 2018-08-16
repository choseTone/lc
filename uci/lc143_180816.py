__author__ = 'wangqc'

'''
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        if head and head.next:
            slow, fast = head.next, head.next.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            front, back = head, self.reverseList(slow)
            while front != slow:
                back_next, back.next = back.next, front.next
                front.next, front, back = back, back.next, back_next
            slow.next = None

    def reverseList(self, node):
        reverse = None
        while node:
            next, node.next = node.next, reverse
            reverse, node = node, next
        return reverse


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
    head = list2node([1, 2, 3, 4, 5])
    sol.reorderList(head)
    print('ans: %s\ntime: %.3fms' % (node2list(head), ((time() - t)) * 1000))
