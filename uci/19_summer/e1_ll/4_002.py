__author__ = 'wangqc'
# https://leetcode.com/problems/add-two-numbers/

from utils import ListNode, Utils


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = node = ListNode(0)
        carry = 0
        while l1 or l2:
            x, y = l1.val if l1 else 0, l2.val if l2 else 0
            carry, z = divmod(x+y+carry, 10)
            node.next = node = ListNode(z)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: node.next = ListNode(carry)
        return head.next


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([2,4,3]), util.list2node([5,6,4]),
    r1 = sol.addTwoNumbers(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([9,9,9]), util.list2node([1]),
    r2 = sol.addTwoNumbers(*t2)
    print(util.node2list(r2))
