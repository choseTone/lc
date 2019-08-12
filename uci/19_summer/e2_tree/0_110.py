__author__ = 'wangqc'
# https://leetcode.com/problems/balanced-binary-tree/

from utils import Utils


class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return True
            lh, rh = height(node.left), height(node.right)
            return max(lh, rh) + 1 if lh and rh and abs(lh - rh) < 2 else False

        return height(root) > 0


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([3, 9, 20, None, None, 15, 7]),
    print(sol.isBalanced(*t1))

    t2 = util.list2tree([1, 2, 2, 3, 3, None, None, 4, 4]),
    print(sol.isBalanced(*t2))
