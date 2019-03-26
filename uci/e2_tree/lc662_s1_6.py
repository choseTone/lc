__author__ = 'wangqc'

# https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/256970/Python-BFS-%2B-Coordinating

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def widthOfBinaryTree(root):
    q, h, left, w = [(root, 0, 0)], 0, 0, 0
    for node, x, y in q:
        if node:
            if h != y: h, left = y, x
            q.append += [(node.left, 2*x, y+1), (node.right, 2*x+1, y+1)]
            w = max(w, x-left+1)
    return w