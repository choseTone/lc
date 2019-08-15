__author__ = 'wangqc'
# https://leetcode.com/problems/maximum-width-of-binary-tree/

from utils import Utils


class Solution:
    def widthOfBinaryTree(self, root):
        q, w, h, l = [(root, 0, 0)], 0, 0, 0
        for node, x, y in q:
            if node:
                if h < y:
                    h, l = y, x
                q += [(node.left, x*2, y+1), (node.right, x*2+1, y+1)]
                w = max(w, x-l+1)
        return w


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1,3,2,5,3,None,9]),
    print(sol.widthOfBinaryTree(*t1))
