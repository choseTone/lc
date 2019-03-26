__author__ = 'wangqc'

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/255029/python-classic-bfs

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    vals, q = [], [(root, 0)]
    for node, d in q:
        if node:
            if len(vals) <= d: vals.append([])
            q += [(node.left, d+1), (node.right, d+1)]
            vals[d] = [node.val] + vals[d] if d & 1 else vals[d] + [node.val]
    return vals