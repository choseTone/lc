__author__ = 'wangqc'
# https://leetcode.com/problems/leaf-similar-trees/

from utils import Utils


class Solution:
    def leafSimilar(self, root1, root2):
        left, right = [], []
        self.preorder(root1, left), self.preorder(root2, right)
        return left == right

    def preorder(self, node, leaves):
        if not (node.left or node.right):
            leaves.append(node.val)
        if node.left:
            self.preorder(node.left, leaves)
        if node.right:
            self.preorder(node.right, leaves)


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2tree([3,5,1,6,2,9,8,None,None,7,4]), \
         util.list2tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]),
    print(sol.leafSimilar(*t1))


