__author__ = 'wangqc'

'''
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if inorder:
            root_i = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_i])
            root.right, root.left = self.buildTree(inorder[root_i+1:], postorder), self.buildTree(inorder[:root_i], postorder)
            return root


if __name__ == '__main__':
    from time import time

    sol = Solution()

    def tree2list(head):
        queue, out, cur = [head], '', 0
        while cur != len(queue):
            node, cur = queue[cur], cur + 1
            if node:
                out += '%d, ' % node.val
                queue += [node.left, node.right]
            else: out += 'null, '
        return out[:-2]

    t = time()
    ans = (sol.buildTree([9,3,15,20,7], [9,15,7,20,3]))
    print('ans: %s\ntime: %.3fms' % (tree2list(ans), ((time() - t)) * 1000))
