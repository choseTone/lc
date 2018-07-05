__author__ = 'wangqc'

'''
654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        max_i = nums.index(max(nums))
        node = TreeNode(nums[max_i])
        node.left = self.constructMaximumBinaryTree(nums[:max_i])
        node.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        return node



if __name__ == '__main__':
    from time import time
    from random import randint

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
    nums = [randint(1, 20) for _ in range(10)]
    ans = tree2list(sol.constructMaximumBinaryTree(nums))
    print('nums: %s\nans: %s\ntime: %.3fms' % (nums, ans, ((time() - t)) * 1000))