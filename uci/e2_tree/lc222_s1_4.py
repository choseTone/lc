__author__ = 'wangqc'

# https://leetcode.com/problems/count-complete-tree-nodes/discuss/255444/Python-Recursive

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def countNodes(root):
    def height(node): return height(node.left) + 1 if node else -1

    h = height(root)
    return 0 if h < 0 else (1<<h) + countNodes(root.right) if height(root.right) == h-1 else countNodes(root.left) + (1<<h-1)