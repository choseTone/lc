__author__ = 'wangqc'

'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
A binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        return bool(self.get_depth(root))

    def get_depth(self, node):
        if not node: return 1
        lh, rh = self.get_depth(node.left), self.get_depth(node.right)
        return max(lh, rh) + 1 if lh and rh and abs(lh - rh) < 2 else False


if __name__ == '__main__':
    from time import time

    sol = Solution()

    def list2tree(nums):
        root = TreeNode(int(nums[0]))
        nodeQueue = [root]
        front, index = 0, 1
        while index < len(nums):
            node, item = nodeQueue[front], nums[index]
            front, index = front + 1, index + 1
            if item:
                node.left = TreeNode(item)
                nodeQueue.append(node.left)
            if index >= len(nums):
                break
            item = nums[index]
            index += 1
            if item:
                node.right = TreeNode(item)
                nodeQueue.append(node.right)
        return root

    t = time()
    tree = list2tree([3, 9, 20, None, None, 15, 7])
    ans = (sol.isBalanced(tree))
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
