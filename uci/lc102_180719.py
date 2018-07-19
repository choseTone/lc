__author__ = 'wangqc'

'''
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        curr, succ, ans = [root] if root else [], [], []
        while curr:
            tmp = []
            for node in curr:
                tmp.append(node.val)
                if node.left:
                    succ.append(node.left)
                if node.right:
                    succ.append(node.right)
            ans.append(tmp)
            curr, succ = succ, []
        return ans


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
    ans = (sol.levelOrder(tree))
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
