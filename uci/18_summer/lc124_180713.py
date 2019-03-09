__author__ = 'wangqc'

'''
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the
parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        self.ans = root.val
        self.max_down(root)
        return self.ans

    def max_down(self, node):
        if not node: return 0
        left, right = max(0, self.max_down(node.left)), max(0, self.max_down(node.right))
        self.ans = max(self.ans, left + node.val + right)
        return max(left, right) + node.val


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
    tree = list2tree([-10, 9, 20, None, None, 15, 7])
    ans = (sol.maxPathSum(tree))
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
