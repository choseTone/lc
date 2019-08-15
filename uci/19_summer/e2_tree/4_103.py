__author__ = 'wangqc'
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from utils import Utils


class Solution:
    def zigzagLevelOrder(self, root):
        layers, q, d = [], [root], 0
        while q:
            nq, layer = [], []
            for node in q:
                if node:
                    layer.append(node.val)
                    nq += [node.left, node.right]
            if layer: layers.append(layer[::-1] if d & 1 else layer)
            q, d = nq, 1 - d
        return layers


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([3, 9, 20, None, None, 15, 7]),
    print(sol.zigzagLevelOrder(*t1))
