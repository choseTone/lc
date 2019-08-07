__author__ = 'wangqc'
# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/

from utils import Utils


class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a and b


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    l1, l2, l3 = util.list2node([8,4,5]), util.list2node([4,1]), util.list2node([5,0,1])
    l2.next.next = l3.next.next.next = l1
    t1 = l2, l3,
    r1 = sol.getIntersectionNode(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([2,6,4]), util.list2node([1,5]),
    r2 = sol.getIntersectionNode(*t2)
    print(util.node2list(r2))
