__author__ = 'wangqc'

# https://leetcode.com/problems/find-k-th-smallest-pair-distance/


class Solution:
    def smallestDistancePair(self, nums, k):
        def over(guess):
            cnt = i = 0
            for j, x in enumerate(nums):
                while x - nums[i] > guess:
                    i += 1
                cnt += j - i
            return cnt >= k

        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mi = lo + hi >> 1
            if over(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,3,1], 1,
    print(sol.smallestDistancePair(*t1))

    t2 = [84,37,32,40,95], 3,
    print(sol.smallestDistancePair(*t2))

    t3 = [0,8,45,88,48,68,28,55,17,24], 11,
    print(sol.smallestDistancePair(*t3))