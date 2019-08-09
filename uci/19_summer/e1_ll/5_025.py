__author__ = 'wangqc'
# https://leetcode.com/problems/reverse-nodes-in-k-group/

from utils import ListNode, Utils


class Solution:
    def reverseKGroup(self, head, k):
        dummy = prev = ListNode(0)
        prev.next = head
        while True:
            node = prev.next
            for _ in range(k):  # ensure left-out nodes remain as they are
                if not node:
                    return dummy.next
                node = node.next
            node, rev = prev.next, None
            for _ in range(k):
                node.next, rev, node = rev, node, node.next
            prev.next.next, prev.next, prev = node, rev, prev.next


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4,5]), 2,
    r1 = sol.reverseKGroup(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([1,2,3,4,5]), 3,
    r2 = sol.reverseKGroup(*t2)
    print(util.node2list(r2))
