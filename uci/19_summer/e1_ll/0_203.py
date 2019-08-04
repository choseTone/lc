__author__ = 'wangqc'
# https://leetcode.com/problems/remove-linked-list-elements/

from utils import ListNode, Utils


class Solution:
    def removeElements(self, head, val):
        dummy = node = ListNode(0)
        dummy.next = head
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,6,3,4,5,6]), 6
    ret = sol.removeElements(*t1)
    print(util.node2list(ret))
