__author__ = 'wangqc'

'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
import bisect

class Solution:
    # find the first number that's smaller than its previous one(read nums from right to left), which will be swapped
    def nextPermutation(self, nums):
        j = -1
        for i in range(1, len(nums))[::-1]:
            if nums[i-1] < nums[i]:
                j = i
                break
        # if there is no such number(whole nums in reversed sorted order), reverse the entire nums as the lowest order
        if j < 0:
            nums[:] = reversed(nums)
        else:
            # use binary search to find the number next larger than nums[j-1] which to be swapped
            nums[j:] = reversed(nums[j:])
            i = bisect.bisect(nums, nums[j-1], j)
            nums[i], nums[j-1] = nums[j-1], nums[i]


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    nums = [randint(1, 20) for _ in range(20)]
    print('nums: %s' % nums)
    t = time()
    sol.nextPermutation(nums)
    print('ans: %s\ntime: %.3fms' % (nums, ((time() - t)) * 1000))