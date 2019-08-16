__author__ = 'wangqc'
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from utils import Utils


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if node in (None, p, q):
                return node
            left, right = dfs(node.left), dfs(node.right)
            return node if left and right else left or right
        return dfs(root)


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    root = util.list2tree([3,5,1,6,2,0,8,None,None,7,4])
    t1 = root, root.left, root.right,
    print(sol.lowestCommonAncestor(*t1).val)

    t2 = root, root.left, root.left.right.right,
    print(sol.lowestCommonAncestor(*t2).val)
