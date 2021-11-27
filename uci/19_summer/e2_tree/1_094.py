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

    # No recursion and O(1) space
    def inorderTraversalMorr(self, root):
        nodes = []
        while root:
            if root.left:
                pred = root.left
                while pred.right and pred.right != root:
                    pred = pred.right
                if pred.right:
                    nodes.append(root.val)
                    pred.right = None
                    root = root.right
                else:
                    pred.right = root
                    root = root.left
            else:
                nodes.append(root.val)
                root = root.right
        return nodes


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2tree([1,2,3,4,5,None,7]),
    print(sol.inorderTraversalRecu(*t1))
    print(sol.inorderTraversalIter(*t1))
    print(sol.inorderTraversalMorr(*t1))

    t2 = util.list2tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]),
    print(sol.inorderTraversalRecu(*t2))
    print(sol.inorderTraversalIter(*t2))
    print(sol.inorderTraversalMorr(*t2))

