__author__ = 'wangqc'


# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        best_gap, N = float('inf'), len(nums)
        for i in range(N - 2):
            head, l, r = nums[i], i+1, N-1
            small, large = head+nums[l]+nums[l+1], head+nums[r-1]+nums[r]
            if small > target:
                best_gap = min(best_gap, small-target, key=abs)
            elif large < target:
                best_gap = min(best_gap, large-target, key=abs)
            else:
                while l < r:
                    gap = head+nums[l]+nums[r] - target
                    if gap < 0:
                        l += 1
                    elif gap > 0:
                        r -= 1
                    else:
                        return target
                    best_gap = min(best_gap, gap, key=abs)
        return target + best_gap


if __name__ == '__main__':
    sol = Solution()

    t1 = [1, 2, 5, 10, 11], 12,
    print(sol.threeSumClosest(*t1))
