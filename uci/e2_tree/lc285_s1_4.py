__author__ = 'wangqc'

# https://leetcode.com/problems/inorder-successor-in-bst/discuss/255475/Java-Simple-Binary

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderSuccessor(root, p):
    cand = None
    while root:
        if root.val > p.val: cand, root = root, root.left
        else: root = root.right
    return cand