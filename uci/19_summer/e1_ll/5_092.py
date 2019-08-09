__author__ = 'wangqc'
# https://leetcode.com/problems/reverse-linked-list-ii/

from utils import ListNode, Utils


class Solution:
    def reverseBetween(self, head, m, n):
        dummy = prev = ListNode(0)
        prev.next = head
        for _ in range(m-1):
            prev = prev.next
        node, rev = prev.next, None
        for _ in range(n-m+1):
            node.next, rev, node = rev, node, node.next
        prev.next.next, prev.next = node, rev
        return dummy.next



if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4,5]), 2, 4,
    r1 = sol.reverseBetween(*t1)
    print(util.node2list(r1))
