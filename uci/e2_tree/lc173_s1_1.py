__author__ = 'wangqc'

# https://leetcode.com/problems/binary-search-tree-iterator/discuss/253715/Java-Stack

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.push(root)

    def next(self):
        if self.hasNext():
            node = self.stack.pop()
            if node.right: self.push(node.right)
            return node.val

    def hasNext(self):
        return bool(self.stack)

    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left