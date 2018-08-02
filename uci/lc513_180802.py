__author__ = 'wangqc'

'''
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.
Example 1:
Input:

    2
   / \
  1   3

Output:
1

Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        queue = [root]
        for node in queue:
            queue += list(filter(None, (node.right, node.left)))
        return node.val


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
    ans = sol.findBottomLeftValue(list2tree([1, 2, 3, 4, None, 5, 6, None, None, 7]))
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
