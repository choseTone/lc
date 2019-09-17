__author__ = 'wangqc'

# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height):
        N, water = len(height), 0
        if N > 2:
            l, r, lmax, rmax = 0, N-1, 0, 0
            while l < r:
                lh, rh = height[l], height[r]
                if lh < rh:
                    if lh < lmax:
                        water += lmax-lh
                    else:
                        lmax = lh
                    l += 1
                else:
                    if rh < rmax:
                        water += rmax-rh
                    else:
                        rmax = rh
                    r -= 1
        return water


if __name__ == '__main__':
    sol = Solution()

    t1 = [0,1,0,2,1,0,1,3,2,1,2,1],
    print(sol.trap(*t1))