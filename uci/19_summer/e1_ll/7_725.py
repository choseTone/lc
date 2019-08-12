__author__ = 'wangqc'

from utils import ListNode, Utils


# https://leetcode.com/problems/split-linked-list-in-parts/

class Solution:
    def splitListToParts(self, root, k):
        node, n, ret = root, 0, []
        while node:
            node, n = node.next, n+1
        d, v = divmod(n, k)
        for i in range(k):
            head = node = ListNode(None)
            for _ in range(d + (i<v)):
                node.next = node = ListNode(root.val)
                root = root.next
            ret.append(head.next)
        return ret


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2node([1, 2, 3]), 5,
    r1 = sol.splitListToParts(*t1)
    print([util.node2list(r) for r in r1])

    t2 = util.list2node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3,
    r2 = sol.splitListToParts(*t2)
    print([util.node2list(r) for r in r2])