__author__ = 'wangqc'

# https://leetcode.com/problems/diameter-of-binary-tree/discuss/253095/Python-Recursion

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    d = 0

    def diameter(node):
        nonlocal d
        if not node: return 0
        l, r = diameter(node.left), diameter(node.right)
        d = max(d, l + r)
        return max(l, r) + 1

    diameter(root)
    return d

