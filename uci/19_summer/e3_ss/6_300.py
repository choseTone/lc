__author__ = 'wangqc'


# https://leetcode.com/problems/longest-increasing-subsequence/

import bisect

class Solution:
    def lengthOfLIS(self, nums):
        lis = []
        for x in nums:
            idx = bisect.bisect_left(lis, x)
            if idx < len(lis):
                lis[idx] = x
            else:
                lis.append(x)
        return len(lis)




if __name__ == '__main__':
    sol = Solution()

    t1 = [10,9,2,5,3,7,101,18],
    print(sol.lengthOfLIS(*t1))
