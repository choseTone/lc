__author__ = 'wangqc'

# https://leetcode.com/problems/number-of-valid-subarrays/


class Solution:
    def validSubarrays(self, nums):
        N, stack, cnt = len(nums), [], 0
        for i, x in enumerate(nums):
            while stack and x < nums[stack[-1]]:
                cnt += i - stack.pop()
            stack.append(i)
        while stack:
            cnt += N - stack.pop()
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,4,2,5,3],
    print(sol.validSubarrays(*t1))

    t2 = [3,2,1],
    print(sol.validSubarrays(*t2))

    t3 = [2,2,2],
    print(sol.validSubarrays(*t3))