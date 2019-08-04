__author__ = 'wangqc'
# https://leetcode.com/problems/delete-node-in-a-linked-list/

from utils import Utils


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    head = node = util.list2node([9,2,6,0,4])
    t1 = 4
    while node.val != t1:
        node = node.next
    sol.deleteNode(node)
    print(util.node2list(head))
