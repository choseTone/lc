__author__ = 'wangqc'

'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
A binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''


'''
If any subtree is not balanced, the whole tree is not balanced. So we can come out with a recursive check to check each subtree.

The check basically checks two things: (1) if both left and right subtree are balanced 
(2) if depth gap between left and right subtree is smaller than two. 
If current subtree pass the check, we return it's depth upwards for parent checking.

To check depth, we need to preserve the value of depth. Since final return value should be a boolean, 
I used a helper routine to perform check.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        return bool(self.check(root))

    def check(self, node):
        if not node: return True
        l, r = self.check(node.left), self.check(node.right)
        return max(l, r) + 1 if l and r and abs(l - r) < 2 else False

'''
Time complexity is O(n) since all nodes are traversed once and space complexity is O(1).
'''