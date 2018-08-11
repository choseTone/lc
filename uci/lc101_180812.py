__author__ = 'wangqc'

'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
   
Note:
Bonus points if you could solve it both recursively and iteratively.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        return self.dfs(root, root)

    def dfs(self, a, b):
        if not (a or b): return True
        if a and b and a.val == b.val:
            return self.dfs(a.left, b.right) and self.dfs(a.right, b.left)
        return False



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
    ans = (sol.isSymmetric(list2tree([1,2,2,3,4,4,3])))
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
