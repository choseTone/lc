__author__ = 'wangqc'

# https://leetcode.com/problems/balanced-binary-tree/discuss/252782/python-recursion

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    return bool(check(root))

def check(node):
    if not node: return True
    l, r = check(node.left), check(node.right)
    return max(l, r) + 1 if l and r and abs(l - r) < 2 else False
