__author__ = 'wangqc'

# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums):
        prev = curr = 0
        for x in nums:
            prev, curr = curr, max(curr, x+prev)
        return curr



if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2,3,1],
    print(sol.rob(*t1))

    t2 = [2,7,9,3,1],
    print(sol.rob(*t2))