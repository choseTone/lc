__author__ = 'wangqc'
# https://leetcode.com/problems/flip-equivalent-binary-trees/

from utils import Utils


class Solution:
    def flipEquiv(self, root1, root2):
        if not (root1 or root2):
            return True
        return root1 and root2 and root1.val == root2.val \
               and (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
                    or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1,2,3,4,5,6,None,None,None,7,8]), \
         util.list2tree([1,3,2,None,6,4,5,None,None,None,None,8,7]),
    print(sol.flipEquiv(*t1))
