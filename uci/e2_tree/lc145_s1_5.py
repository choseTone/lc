__author__ = 'wangqc'

# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/256251/Python-Recursion-and-Iteration

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorderTraversalRecu(root):
    return postorderTraversalRecu(root.left) + postorderTraversalRecu(root.right) + [root.val] if root else []

def postorderTraversalIter(root):
    nodes, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            nodes.insert(0, node.val)
            stack += [node.left, node.right]
    return nodes