__author__ = 'wangqc'
# https://leetcode.com/problems/count-complete-tree-nodes/

from utils import Utils


class Solution:
    def countNodes(self, root):
        def height(node):
            return height(node.left) + 1 if node else -1
        h = height(root)
        return 0 if h < 0 \
            else (1<<h) + self.countNodes(root.right) if height(root.right) == h-1 \
            else self.countNodes(root.left) + (1<<h-1)

if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([1,2,3,4,5,6]),
    print(sol.countNodes(*t1))

    t2 = util.list2tree([1,2,3,4,5,6,7,8]),
    print(sol.countNodes(*t2))
