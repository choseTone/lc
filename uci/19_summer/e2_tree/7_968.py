__author__ = 'wangqc'
# https://leetcode.com/problems/binary-tree-cameras/

from utils import Utils


class Solution:
    def minCameraCover(self, root):
        self.cnt = 0

        def dfs(node):
            if not node:
                return 2
            if not (node.left or node.right):
                return 0
            l, r = dfs(node.left), dfs(node.right)
            if not l * r:
                self.cnt += 1
                return 1
            return ((l | r) & 1) << 1

        return (not dfs(root)) + self.cnt


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([0, 0, None, 0, 0]),
    print(sol.minCameraCover(*t1))

    t2 = util.list2tree([0, 0, None, 0, None, 0, None, None, 0]),
    print(sol.minCameraCover(*t2))
