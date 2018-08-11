__author__ = 'wangqc'

'''
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines 
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis 
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) 
the container can contain is 49.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    def maxArea(self, height):
        ans, l, r = 0, 0, len(height) - 1
        while l < r:
            hl, hr = height[l], height[r]
            ans = max(ans, min(hl, hr) * (r - l))
            if hl < hr: l += 1
            else: r -= 1
        return ans


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    height = [randint(1, 100) for _ in range(20)]

    t = time()
    ans = sol.maxArea(height)
    print('height: %s\nans: %s\ntime: %.3fms' % (height, ans, ((time() - t)) * 1000))

