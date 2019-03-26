__author__ = 'wangqc'

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/255047/Python-DFS

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def flatten(root):
    def dfs(node):
        if node.right: dfs(node.right)
        if node.left:
            dfs(node.left)
            right = node.right
            node.left, node.right = None, node.left
            while node.right: node = node.right
            node.right = right
    if root: dfs(root)