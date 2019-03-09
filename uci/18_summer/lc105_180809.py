__author__ = 'wangqc'

'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        if inorder:
            root_i = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_i])
            root.left, root.right = self.buildTree(preorder, inorder[:root_i]), self.buildTree(preorder, inorder[root_i+1:])
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
    ans = (sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))
    print('ans: %s\ntime: %.3fms' % (tree2list(ans), ((time() - t)) * 1000))
