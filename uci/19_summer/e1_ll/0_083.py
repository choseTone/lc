__author__ = 'wangqc'
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from utils import ListNode, Utils


class Solution:
    def deleteDuplicates(self, head):
        node = head
        while node and node.next:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,1,2,3,3]),
    ret = sol.deleteDuplicates(*t1)
    print(util.node2list(ret))
