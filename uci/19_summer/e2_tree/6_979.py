__author__ = 'wangqc'
# https://leetcode.com/problems/distribute-coins-in-binary-tree/

from utils import Utils


class Solution:
    def distributeCoins(self, root):
        self.cnt = 0
        def dfs(node):
            if not node:
                return 0
            lbal, rbal = dfs(node.left), dfs(node.right)
            self.cnt += abs(lbal) + abs(rbal)
            return node.val + lbal + rbal - 1
        dfs(root)
        return self.cnt


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1,0,0,None,3]),
    print(sol.distributeCoins(*t1))
