__author__ = 'wangqc'

# https://leetcode.com/problems/sliding-window-maximum/


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, K):
        q, maxes = deque(), []
        for i, x in enumerate(nums):
            while q and nums[q[-1]] < x:
                q.pop()
            q.append(i)
            if q[0] + K == i:
                q.popleft()
            if i >= K-1:
                maxes.append(nums[q[0]])
        return maxes


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,3,-1,-3,5,3,6,7], 3,
    print(sol.maxSlidingWindow(*t1))