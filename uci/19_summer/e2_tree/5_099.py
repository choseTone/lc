__author__ = 'wangqc'
# https://leetcode.com/problems/recover-binary-search-tree/

from utils import TreeNode, Utils


class Solution:
    def recoverTree(self, root):
        self.first = self.second = None
        self.prev = TreeNode(float('-inf'))
        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev.val >= node.val:
                    self.first = self.first or self.prev
                    self.second = node
                self.prev = node
                inorder(node.right)
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    root = node = util.list2tree([3,1,4,None,None,2])
    sol.recoverTree(node)
    print(util.tree2list(node))

