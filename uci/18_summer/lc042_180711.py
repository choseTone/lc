__author__ = 'wangqc'

'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it 
is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water 
(blue section) are being trapped. Thanks Marcos for contributing this image!
'''


class Solution:
    # o(2n) time; o(2n) space
    def trap_two_passes(self, height):
        n = len(height)
        if n < 3: return 0
        left, right = [height[0]], [height[n-1]]
        for i in range(1, n):
            left.append(max(left[-1], height[i]))
            right = [max(right[0], height[n-1-i])] + right
        return sum(min(left[i], right[i]) - height[i] for i in range(n))

    # o(n-2n) time; o(n) space
    def trap_stack(self, height):
        n, ans = len(height), 0
        if n > 2:
            stack = [0]
            for i in range(1, n):
                while stack and height[i] > height[stack[-1]]:
                    trap = stack.pop()
                    if not stack: break
                    ans += (min(height[i], height[stack[-1]]) - height[trap]) * (i - stack[-1] - 1)
                stack.append(i)
        return ans

    # o(n) time; o(1) space
    def trap_two_pointers(self, height):
        n, ans = len(height), 0
        if n < 3: return ans
        l, r, lmax, rmax = 0, n - 1, 0, 0
        while l <= r:
            lh, rh = height[l], height[r]
            if lh < rh:
                if lh < lmax: ans += lmax - lh
                else: lmax = lh
                l += 1
            else:
                if rh < rmax: ans += rmax - rh
                else: rmax = rh
                r -= 1
        return ans


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    nums = [randint(0, 100) for _ in range(10**4)]
    t0 = time()
    ans = sol.trap_two_passes(nums)
    t1 = time()
    ans1 = sol.trap_two_passes(nums)
    t2 = time()
    ans2 = sol.trap_stack(nums)
    t3 = time()
    ans3 = sol.trap_two_pointers(nums)
    t4 = time()
    # nums is a random array with a size of 10**4
    # sol1 150.87ms; sol2 5.60ms; sol3 1.56ms
    print('ans1: %s\ntime: %.3fms' % (ans1, ((t2 - t1)) * 1000))
    print('ans2: %s\ntime: %.3fms' % (ans2, ((t3 - t2)) * 1000))
    print('ans3: %s\ntime: %.3fms' % (ans3, ((t4 - t3)) * 1000))