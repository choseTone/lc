__author__ = 'wangqc'

# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/256224/python-dfs-with-quite-detailed-explanation

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distributeCoins(root):
    def dfs(node):
        if not node: return 0, 0
        (lbal, lcnt), (rbal, rcnt) = dfs(node.left), dfs(node.right)
        bal = node.val + lbal + rbal - 1
        return bal, lcnt + rcnt + abs(bal)
    return dfs(root)[1]