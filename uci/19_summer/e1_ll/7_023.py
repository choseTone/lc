__author__ = 'wangqc'

from utils import ListNode, Utils


# https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def mergeKLists(self, lists):
        k, d = len(lists), 1
        while d < k:
            for i in range(0, k-d, d<<1):
                lists[i] = self.merge2Lists(lists[i], lists[i+d])
            d <<= 1
        return (lists or None) and lists[0]

    def merge2Lists(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge2Lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge2Lists(l1, l2.next)
            return l2


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = [util.list2node([1, 4, 5]), util.list2node([1, 3, 4]), util.list2node([2, 6])],
    r1 = sol.mergeKLists(*t1)
    print(util.node2list(r1))