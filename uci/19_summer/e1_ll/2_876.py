__author__ = 'wangqc'
# https://leetcode.com/problems/middle-of-the-linked-list/

from utils import Utils


class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4,5]),
    r1 = sol.middleNode(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([1,2,3,4,5,6]),
    r2 = sol.middleNode(*t2)
    print(util.node2list(r2))
