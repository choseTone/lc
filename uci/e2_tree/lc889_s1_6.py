__author__ = 'wangqc'

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/256466/Python-Recursion-DandC

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructFromPrePost(pre, post):
    if not pre: return None
    root = TreeNode(pre[0])
    if len(pre) > 1:
        lcnt = post.index(pre[1]) + 1
        root.left = constructFromPrePost(pre[1:lcnt+1], post[:lcnt])
        root.right = constructFromPrePost(pre[lcnt+1:], post[lcnt:-1])
    return root