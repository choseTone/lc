__author__ = 'wangqc'

# https://leetcode.com/problems/recover-binary-search-tree/discuss/256055/Python-Inorder-Traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recoverTree(root):
    first, second, prev = None, None, TreeNode(float('-inf'))
    def inorder(node):
        nonlocal first, second, prev
        if node:
            inorder(node.left)
            if not first and prev.val >= node.val:
                first = prev
            if first and prev.val >= node.val:
                second = node
            prev = node
            inorder(node.right)
    inorder(root)
    first.val, second.val = second.val, first.val