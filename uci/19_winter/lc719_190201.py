__author__ = 'wangqc'

'''
719. Find K-th Smallest Pair Distance

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined 
as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''


class Solution:
    def smallestDistancePair(self, nums, k):
        # if guess cnt more than k, overflow, reduce hi
        def overflow(guess):
            cnt = i = 0
            for j, x in enumerate(nums):
                while x - nums[i] > guess: i += 1
                cnt += j - i  # slide window to cnt the distance <= guess
            return cnt >= k
        nums.sort()
        lo, hi = 0, nums[-1]-nums[0]
        while lo < hi:
            mi = lo + hi >> 1
            if overflow(mi): hi = mi
            else: lo = mi + 1
        return lo

if __name__ == '__main__':
    sol = Solution()
    argv = [1,3,1], 1
    ans = sol.smallestDistancePair(*argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

