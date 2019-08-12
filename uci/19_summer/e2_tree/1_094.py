__author__ = 'wangqc'
# https://leetcode.com/problems/binary-tree-inorder-traversal/

from utils import Utils


class Solution:
    def inorderTraversalRecu(self, root):
        return self.inorderTraversalRecu(root.left) + [root.val] + self.inorderTraversalRecu(root.right) if root else []

    def inorderTraversalIter(self, root):
        nodes, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            nodes.append(stack[-1].val)
            root = stack.pop().right
        return nodes


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2tree([1,2,3,4,5,None,7]),
    print(sol.inorderTraversalRecu(*t1))
    print(sol.inorderTraversalIter(*t1))

    t2 = util.list2tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]),
    print(sol.inorderTraversalRecu(*t2))
    print(sol.inorderTraversalIter(*t2))

