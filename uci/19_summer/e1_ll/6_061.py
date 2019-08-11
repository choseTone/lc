__author__ = 'wangqc'
# https://leetcode.com/problems/rotate-list/

from utils import ListNode, Utils


class Solution:
    def rotateRight(self, head, k):
        dummy = node = ListNode(0)
        node.next, n = head, 0
        while node.next:
            node, n = node.next, n+1
        node, k = dummy.next, n and k % n
        if not (k and head and head.next):
            return head
        for i in range(n-1):
            if i == n-k-1:
                node.next, node, dummy.next = None, node.next, node.next
            else:
                node = node.next
        node.next = head
        return dummy.next



if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2,3,4,5]), 6,
    r1 = sol.rotateRight(*t1)
    print(util.node2list(r1))
