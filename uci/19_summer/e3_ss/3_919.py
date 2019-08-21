__author__ = 'wangqc'

# https://leetcode.com/problems/next-greater-element-ii/


import heapq


class Solution:
    def nextGreaterElements(self, nums):
        N = len(nums)
        stack, idx = [], [-1] * N

        def scan(right):
            for i, x in enumerate(nums):
                while stack and nums[stack[-1]] < x:
                    idx[stack.pop()] = x
                if right:
                    stack.append(i)

        scan(True), scan(False)
        return idx


if __name__ == '__main__':
    sol = Solution()

    t1 = [1, 2, 3, 4, 5, 4, 3, 2, 1],
    print(sol.nextGreaterElements(*t1))
