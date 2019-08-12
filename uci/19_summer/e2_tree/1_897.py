__author__ = 'wangqc'
# https://leetcode.com/problems/increasing-order-search-tree/

from utils import TreeNode, Utils


class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.curr.right = self.curr = node
                inorder(node.right)

        ret = self.curr = TreeNode(None)
        inorder(root)
        return ret.right


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]),
    r1 = sol.increasingBST(*t1)
    print(util.tree2list(r1))
