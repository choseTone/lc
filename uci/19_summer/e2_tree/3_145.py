__author__ = 'wangqc'
# https://leetcode.com/problems/binary-tree-postorder-traversal/

from utils import Utils


class Solution:
    def postorderTraversalRecu(self, root):
        return self.postorderTraversalRecu(root.left) + self.postorderTraversalRecu(root.right) + [root.val] if root else []

    def postorderTraversalIter(self, root):
        nodes, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                nodes.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return nodes[::-1]


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([5, 3, 6, 2, 4, None, 7]),
    print(sol.postorderTraversalRecu(*t1))
    print(sol.postorderTraversalIter(*t1))
