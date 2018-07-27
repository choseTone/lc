__author__ = 'wangqc'

'''
416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such 
that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''


class Solution:
    # dfs from larger number to smaller number
    def canPartition(self, nums):
        sum_nums = sum(nums)
        if sum_nums & 1: return False
        target = sum_nums >> 1
        return self.dfs(sorted(nums, reverse=True), 0, [target, target])

    def dfs(self, nums, idx, targets):
        for i in range(2):
            if targets[i] >= nums[idx]:
                targets[i] -= nums[idx]
                if targets[i] == 0 or self.dfs(nums, idx+1, targets):
                    return True
                targets[i] += nums[idx]
        return False


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.canPartition([1, 2, 3, 4, 5, 6, 7])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
