__author__ = 'wangqc'

'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        k, d = len(lists), 1
        while d < k:
            for i in range(0, k-d, d*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+d])
            d *= 2
        return lists and lists[0]

    def merge2Lists(self, l1, l2):
        head = node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 or l2
        return head.next



if __name__ == '__main__':
    from time import time

    def convert(lists):
        nodes = []
        for l in lists:
            head = node = ListNode(0)
            for val in l:
                node.next = ListNode(val)
                node = node.next
            nodes.append(head.next)
        return nodes

    def revert(node):
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans

    sol = Solution()
    t = time()
    ans = sol.mergeKLists(convert([[1, 4, 5], [1, 3, 4], [2, 6]]))
    print('ans: %s\ntime: %.3fms' % (revert(ans), ((time() - t)) * 1000))