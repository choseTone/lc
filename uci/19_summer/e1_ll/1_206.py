__author__ = 'wangqc'
# https://leetcode.com/problems/reverse-linked-list/

from utils import Utils


class Solution:
    def reverseListIter(self, head):
        rev = None
        while head:
            head.next, rev, head = rev, head, head.next
        return rev

    def reverseListRecu(self, head):
        if not (head and head.next):
            return head
        node, head.next.next, head.next = self.reverseListRecu(head.next), head, None
        return node


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4,5]),
    r1 = sol.reverseListIter(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([1,2,3,4,5]),
    r2 = sol.reverseListRecu(*t2)
    print(util.node2list(r2))
