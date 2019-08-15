__author__ = 'wangqc'
# https://leetcode.com/problems/path-sum-ii/

from utils import Utils


class Solution:
    def pathSum(self, root, target):
        if not root:
            return []
        if not (root.left or root.right) and root.val == target:
            return [[root.val]]
        return [[root.val] + path
                for path in self.pathSum(root.left, target-root.val) + self.pathSum(root.right, target-root.val)]


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22
    print(sol.pathSum(*t1))
