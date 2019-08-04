__author__ = 'wangqc'
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from utils import ListNode, Utils


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = fast = slow = ListNode(0)
        dummy.next = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4,5]), 5
    ret = sol.removeNthFromEnd(*t1)
    print(util.node2list(ret))
