__author__ = 'wangqc'
# https://leetcode.com/problems/add-two-numbers-ii/

from utils import ListNode, Utils


class Solution:
    def addTwoNumbers(self, l1, l2):
        x = y = 0
        while l1:
            x, l1 = x*10+l1.val, l1.next
        while l2:
            y, l2 = y*10+l2.val, l2.next
        z, head, node = x+y, ListNode(0), None
        while z:
            head, z = ListNode(z % 10), z // 10
            head.next, node = node, head
        return head


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([7,2,4,3]), util.list2node([5,6,4]),
    r1 = sol.addTwoNumbers(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([9,9,9]), util.list2node([1]),
    r2 = sol.addTwoNumbers(*t2)
    print(util.node2list(r2))
