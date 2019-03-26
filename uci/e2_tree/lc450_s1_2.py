__author__ = 'wangqc'

# https://leetcode.com/problems/delete-node-in-a-bst/discuss/254235/python-recursion

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deleteNode(root, key):
    if not root: return None
    if root.val > key:
        root.left = deleteNode(root.left, key)
    elif root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        if not (root.left and root.right): return root.left or root.right
        root.val = findCloset(root.right).val
        root.right = deleteNode(root.right, root.val)
    return root

def findCloset(node):
    while node.left:
        node = node.left
    return node