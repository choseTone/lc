__author__ = 'wangqc'

# https://leetcode.com/problems/binary-search-tree-iterator/

from utils import TreeNode, Utils


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.push(root)

    def next(self):
        if self.hasNext():
            node = self.stack.pop()
            if node.right:
                self.push(node.right)
            return node.val

    def hasNext(self):
        return bool(self.stack)

    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left


if __name__ == '__main__':
    util = Utils()
    obj = BSTIterator(util.list2tree([7, 3, 15, None, None, 9, 20]))
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
