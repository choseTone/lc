__author__ = 'wangqc'


# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums, m):
        lo, hi = max(nums), sum(nums)

        def capable(s):
            val, cnt = 0, 1
            for x in nums:
                val += x
                if val > s:
                    cnt += 1
                    val = x
                if cnt > m:
                    return False
            return True

        while lo < hi:
            mid = lo + hi >> 1
            if capable(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    sol = Solution()

    t1 = [7,2,5,10,8], 2,
    print(sol.splitArray(*t1))
