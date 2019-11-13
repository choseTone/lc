__author__ = 'wangqc'
# https://leetcode.com/problems/reorder-list/

from utils import Utils


class Solution:
    def reorderList(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        rev, node = None, head
        while slow:
            slow.next, rev, slow = rev, slow, slow.next  # second half to be cut off later
        while rev:
            node.next, rev.next, node, rev = rev, node.next, node.next, rev.next
        if node:
            node.next = None  # cut off the second half
        return head


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4]),
    r1 = sol.reorderList(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([1,2,3,4,5]),
    r2 = sol.reorderList(*t2)
    print(util.node2list(r2))
