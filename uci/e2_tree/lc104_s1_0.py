__author__ = 'wangqc'

# https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/252775/python-one-line

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    return max(maxDepth(root.left),maxDepth(root.right)) + 1 if root else 0