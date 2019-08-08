__author__ = 'wangqc'
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from utils import ListNode, Utils


class Solution:
    def deleteDuplicates(self, head):
        prev = dummy = ListNode(0)
        prev.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head = head.next
            else:
                prev, head = prev.next, head.next
        return dummy.next


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,1,2,3,4,4,5]),
    r1 = sol.deleteDuplicates(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([1,2,3,3,3]),
    r2 = sol.deleteDuplicates(*t2)
    print(util.node2list(r2))
