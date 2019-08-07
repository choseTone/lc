__author__ = 'wangqc'
# https://leetcode.com/problems/merge-two-sorted-lists/

from utils import ListNode, Utils


class Solution:
    def mergeTwoListsIter(self, l1, l2):
        dummy = node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                node.next = node = l1
                l1 = l1.next
            else:
                node.next = node = l2
                l2 = l2.next
        node.next = l1 or l2
        return dummy.next

    def mergeTwoListsRecu(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoListsRecu(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecu(l1, l2.next)
            return l2


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    l1, l2 = util.list2node([1,2,4]), util.list2node([1,3,4])
    t1 = l1, l2,
    r1 = sol.mergeTwoListsIter(*t1)
    print(util.node2list(r1))

    l3, l4 = util.list2node([1, 2, 4]), util.list2node([1, 3, 4])
    t2 = l3, l4,
    r2 = sol.mergeTwoListsRecu(*t2)
    print(util.node2list(r2))
