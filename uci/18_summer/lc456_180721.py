__author__ = 'wangqc'

'''
456. 132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and 
ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern
in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]
Output: False
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: [3, 1, 4, 2]
Output: True
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]
Output: True
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''


class Solution:
    # store potential 1 in mins and 2 in mids, search potential 3 as cur from back of the nums; cur > mids > mins
    def find132pattern(self, nums):
        if len(nums) < 3: return False
        mins, mids = [nums[0]], []
        for n in nums[1:]:
            mins.append(min(mins[-1], n))
        for i in range(len(nums))[::-1]:
            cur = nums[i]
            if cur > mins[i]:
                while mids and mids[-1] <= mins[i]:
                    mids.pop()
                if mids and mids[-1] < cur:
                    return True
                mids.append(cur)
        return False


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.find132pattern([3, 1, 4, 2])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
