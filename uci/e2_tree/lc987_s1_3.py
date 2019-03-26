__author__ = 'wangqc'

# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/255039/Python-DFS-%2B-Hash-Map
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def verticalTraversal(root):
    vals = collections.defaultdict(lambda: collections.defaultdict(list))
    def dfs(node, x, y):
        if node:
            vals[x][y].append(node.val)
            dfs(node.left, x-1, y+1), dfs(node.right, x+1, y+1)
    dfs(root, 0, 0)
    return [[v for y in sorted(vals[x]) for v in sorted(vals[x][y])] for x in sorted(vals)]