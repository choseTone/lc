__author__ = 'wangqc'
# https://leetcode.com/problems/diameter-of-binary-tree/

from utils import Utils


class Solution:
    def diameterOfBinaryTree(self, root):
        self.d = 0
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self.d = max(self.d, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.d


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1, 2, 3, 4, 5]),
    print(sol.diameterOfBinaryTree(*t1))
