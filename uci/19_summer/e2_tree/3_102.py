__author__ = 'wangqc'
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from utils import Utils


class Solution:
    def levelOrder(self, root):
        layers, q, nq = [], [root], []
        while q:
            layers.append([])
            for node in q:
                layers[-1].append(node.val)
                if node.left: nq.append(node.left)
                if node.right: nq.append(node.right)
            q, nq = nq, []
        return layers


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([3,9,20,None,None,15,7]),
    print(sol.levelOrder(*t1))
