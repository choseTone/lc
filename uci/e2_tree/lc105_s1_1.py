__author__ = 'wangqc'

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/253611/python-simple-recursion

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if inorder:
        root_val = preorder.pop(0)
        idx, root = inorder.index(root_val), TreeNode(root_val)
        root.left, root.right = buildTree(preorder, inorder[:idx]), buildTree(preorder, inorder[idx + 1:])
        return root