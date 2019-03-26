__author__ = 'wangqc'

'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
'''

'''
Preroder places a root node at the head(preorder[0]). So for each recursion where we need to build a subree, 
e pop a node from preroder which would be the root node.
Inorder places left tree's nodes at the left of the root node and right tree's nodes at the right. 
So we pass inorder[:idx of root] to left tree's recursion and inorder[idx +1:] to the right's.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            root_val = preorder.pop(0)
            idx, root = inorder.index(root_val), TreeNode(root_val)
            root.left, root.right = self.buildTree(preorder, inorder[:idx]), self.buildTree(preorder, inorder[idx + 1:])
            return root

'''
The recursive equation is T(n) = 2T(n/2) + c so time complexity is O(n).
'''