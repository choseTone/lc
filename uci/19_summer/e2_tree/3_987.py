__author__ = 'wangqc'
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from utils import Utils
from collections import defaultdict


class Solution:
    def verticalTraversal(self, root):
        tree = defaultdict(lambda: defaultdict(list))

        def dfs(node, x, y):
            if node:
                tree[x][y].append(node.val)
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)
        return [[v for y in sorted(tree[x]) for v in sorted(tree[x][y])] for x in sorted(tree)]


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1, 2, 3, 4, 5, 6, 7]),
    print(sol.verticalTraversal(*t1))
