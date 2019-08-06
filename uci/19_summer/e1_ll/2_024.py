__author__ = 'wangqc'
# https://leetcode.com/problems/swap-nodes-in-pairs/

from utils import ListNode, Utils


class Solution:
    def swapPairs(self, head):
        dummy = prev = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            one, two = prev.next, prev.next.next
            one.next, two.next, prev.next = two.next, one, two
            prev = prev.next.next  # prev.next.next is one
        return dummy.next


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4]),
    r1 = sol.swapPairs(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([1,2,3]),
    r2 = sol.swapPairs(*t2)
    print(util.node2list(r2))
