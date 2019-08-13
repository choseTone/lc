__author__ = 'wangqc'
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from utils import TreeNode, Utils


class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return
        # original "preorder" should be pass down to the sub recursion instead of passing a new "preorder"
        root_val = preorder.pop(0)
        root, root_id = TreeNode(root_val), inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:root_id])
        root.right = self.buildTree(preorder, inorder[root_id + 1:])
        return root


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7],
    r1 = sol.buildTree(*t1)
    print(util.tree2list(r1))
