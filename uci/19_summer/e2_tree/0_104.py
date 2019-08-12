__author__ = 'wangqc'
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from utils import Utils


class Solution:
    def maxDepth(self, root):
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0



if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2tree([3,9,20,None,None,15,7]),
    print(sol.maxDepth(*t1))

