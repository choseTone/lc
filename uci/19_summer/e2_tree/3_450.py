__author__ = 'wangqc'
# https://leetcode.com/problems/flip-equivalent-binary-trees/

from utils import Utils


class Solution:
    def deleteNode(self, root, key):
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not (root.left and root.right):
                return root.left or root.right
            root.val = self.find_next(root.right).val
            root.right = self.deleteNode(root.right, root.val)
        return root

    def find_next(self, node):
        while node.left:
            node = node.left
        return node


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([5, 3, 6, 2, 4, None, 7]), 3,
    r1 = sol.deleteNode(*t1)
    print(util.tree2list(r1))
