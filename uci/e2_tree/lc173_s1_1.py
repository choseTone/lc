__author__ = 'wangqc'

'''
951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

Example 1:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
'''

'''
#951 is largely combination of #100(Same Tree) and #101(Symmetric Tree).
For each pair of trees, both tree should exist or neither of them exist. So first logic true condition is not(r1 or r2);
If both tree exist, their root value should equal, so the second logic true condition is r1 and r2 and r1.val == r2.val;
Finally we compare subtrees.
If two pairs of next level trees are the same, left branches of two tree and right branches of two tree should be 
flipEquived or flipEquiv(r1.left, r2.left) and flipEquiv(r1.right, r2.right) should return True.
Otherwise two pairs of next level trees are symmetric, or flipEquiv(r1.left, r2.right) and flipEquiv(r1.right, r2.left) should return True.

All other occasions returns False
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flipEquiv(self, r1, r2):
        return bool(not (r1 or r2)
                    or r1 and r2 and r1.val == r2.val
                    and (self.flipEquiv(r1.left, r2.left) and self.flipEquiv(r1.right, r2.right)
                         or self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left)))

'''
The recursion equation is T(n) = 4T(n/2) + c so time complexity is O(n^2).
'''