__author__ = 'wangqc'

'''
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the 
"root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that 
"all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses 
were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        val = self.rob_sub(root)
        return max(val[0], val[1])

    def rob_sub(self, node):
        if not node: return [0, 0]
        left, right = self.rob_sub(node.left), self.rob_sub(node.right)
        return [node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])]


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

    ans = sol.rob(list2tree([3, 2, 3, None, 3, None, 1]))
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
