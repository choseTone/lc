__author__ = 'wangqc'

'''
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


class Solution:
    # no extra space and o(n) solution
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i]:
                next_i = nums[i] - 1
                while nums[next_i]:
                    nums[next_i], next_i = 0, nums[next_i] - 1
        return [i + 1 for i in range(n) if nums[i]]


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
