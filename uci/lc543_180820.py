__author__ = 'wangqc'

'''
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the 
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
Note: The length of path between two nodes is represented by the number of edges between them.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        self.diameter(root)
        return self.ans

    def diameter(self, node):
        if not node: return 0
        left, right = self.diameter(node.left), self.diameter(node.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1




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
    ans = sol.diameterOfBinaryTree(list2tree([1,2,3,4,5]))
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
