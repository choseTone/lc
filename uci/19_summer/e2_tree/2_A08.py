__author__ = 'wangqc'
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

import bisect
from utils import TreeNode, Utils


class Solution:
    def bstFromPreorder(self, preorder):
        def dc(l, r):
            if l < r:
                root = TreeNode(preorder[l])
                m = bisect.bisect(preorder, preorder[l], l+1, r)
                root.left, root.right = dc(l+1, m), dc(m, r)
                return root
        return dc(0, len(preorder))


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = [8,5,1,7,10,12],
    r1 = sol.bstFromPreorder(*t1)
    print(util.tree2list(r1))
