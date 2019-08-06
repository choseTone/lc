__author__ = 'wangqc'
# https://leetcode.com/problems/reorder-list/

from utils import ListNode, Utils


class Solution:
    def reorderList(self, head):
        dummy = slow = fast = ListNode(0)
        dummy.next = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next, slow, rev = None, slow.next, None    # break from half
        while slow:                 # reverse second half which could be shorter
            slow.next, rev, slow = rev, slow, slow.next
        while rev:                  # merge two halves
            head.next, rev.next, head, rev = rev, head.next, head.next, rev.next
        return dummy.next


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4]),
    r1 = sol.reorderList(*t1)
    print(util.node2list(r1))

    t2 = util.list2node([1,2,3,4,5]),
    r2 = sol.reorderList(*t2)
    print(util.node2list(r2))
