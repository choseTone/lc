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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList_iter(self, head):
        reverse = None
        while head:
            next_node, head.next = head.next, reverse
            reverse, head = head, next_node
        return reverse

    def reverseList_recur(self, head):
        def recur(node, reverse_node):
            if not node: return reverse_node
            next_node, node.next = node.next, reverse_node
            return recur(next_node, node)
        return recur(head, None)


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
    ans = sol.reverseList_recur(list2node([1, 0, 6, 8, 1, 5]))
    print('ans: %s\ntime: %.3fms' % (node2list(ans), ((time() - t)) * 1000))
