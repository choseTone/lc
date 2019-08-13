__author__ = 'wangqc'
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

from utils import TreeNode, Utils


class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) > 1:
            lcnt = post.index(pre[1]) + 1
            root.left = self.constructFromPrePost(pre[1:lcnt+1], post[:lcnt])
            root.right = self.constructFromPrePost(pre[lcnt+1:], post[lcnt:-1])
        return root

if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = [1,2,4,5,3,6,7], [4,5,2,6,7,3,1],
    r1 = sol.constructFromPrePost(*t1)
    print(util.tree2list(r1))
