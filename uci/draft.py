__author__ = 'wangqc'


class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        nums = [a * n**2 + b * n + c for n in nums]
        l, r = 0, len(nums) - 1
        ans = [0] * (r + 1)
        i, d = (l, 1) if a < 0 else (r, -1)
        while l <= r:
            if nums[l] * d < nums[r] * d:
                ans[i] = nums[l]
                l += 1
            else:
                ans[i] = nums[r]
                r -= 1
            i += d
        return ans

sol = Solution()
print(sol.sortTransformedArray([-4,-2,2,4], 1, 3, 5))