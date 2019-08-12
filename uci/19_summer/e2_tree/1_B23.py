__author__ = 'wangqc'
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

from utils import TreeNode, Utils


class Solution:
    def lcaDeepestLeaves(self, root):
        def dfs(node, d):
            if not node:
                return None, d
            ln, ld, rn, rd = *dfs(node.left, d + 1), *dfs(node.right, d + 1)
            return (ln, ld) if ld > rd \
                else (rn, rd) if ld < rd \
                else (node, ld)

        return dfs(root, 0)[0]


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1, 2, 3, 4]),
    r1 = sol.lcaDeepestLeaves(*t1)
    print(util.tree2list(r1))

    t2 = util.list2tree([1, 2, 3, 4, 5]),
    r2 = sol.lcaDeepestLeaves(*t2)
    print(util.tree2list(r2))
