__author__ = 'wangqc'

'''
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

'''
Help to understand tree's basic recursion rule.
On the base floor when node is null, return 0.
On the other floors, return the larger depth of left node and right node + 1(current floor) as per max depth request.
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