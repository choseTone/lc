__author__ = 'wangqc'
# https://leetcode.com/problems/sort-list/

from utils import Utils


class Solution:
    # merge sort
    def sortList(self, head):
        if not (head and head.next):
            return head
        mid, right = head, head.next
        while right and right.next:
            mid, right = mid.next, right.next.next
        mid.next, mid = None, mid.next
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([4,2,1,3]),
    r1 = sol.sortList(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([-1,5,3,4,0]),
    r2 = sol.sortList(*t2)
    print(util.node2list(r2))
