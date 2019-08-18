__author__ = 'wangqc'
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from utils import Utils


class Solution:
    def sumNumbers(self, root):
        def dfs(node, val):
            if not node:
                return 0
            val = val * 10 + node.val
            return val if not (node.left or node.right) else dfs(node.left, val) + dfs(node.right, val)
        return dfs(root, 0)


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1,2,3]),
    print(sol.sumNumbers(*t1))

    t2 = util.list2tree([4,9,0,5,1]),
    print(sol.sumNumbers(*t2))
