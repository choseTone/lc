__author__ = 'wangqc'

# https://leetcode.com/problems/flip-equivalent-binary-trees/discuss/253619/python-one-line-recursion

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def flipEquiv(r1, r2):
    return bool(not (r1 or r2)
                or r1 and r2 and r1.val == r2.val
                and (flipEquiv(r1.left, r2.left) and flipEquiv(r1.right, r2.right)
                     or flipEquiv(r1.left, r2.right) and flipEquiv(r1.right, r2.left)))