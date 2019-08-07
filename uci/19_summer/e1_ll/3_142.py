__author__ = 'wangqc'
# https://leetcode.com/problems/linked-list-cycle-ii/

from utils import Utils


class Solution:
    def detectCycle(self, head):
        a = b = c = head
        while a and a.next:
            a, b = a.next.next, b.next
            if a == b:
                while b != c:
                    b, c = b.next, c.next
                return c
        return None


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    l1, l2 = util.list2node([3,2,0]), util.list2node([4])
    l2.next, l1.next.next = l1.next, l2
    t1 = l1,
    r1 = sol.detectCycle(*t1)
    print(r1 and r1.val)

    t2 = util.list2node([1]),
    r2 = sol.detectCycle(*t2)
    print(r2 and r2.val)
