__author__ = 'wangqc'
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from utils import Utils


# in-place solution
class Solution:
    def flatten(self, root):
        if not root:
            return
        if root.right:
            self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            right, root.left, root.right = root.right, None, root.left
            while root.right:
                root = root.right
            root.right = right


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1, 2, 5, 3, 4, None, 6])
    sol.flatten(t1)
    print(util.tree2list(t1))
