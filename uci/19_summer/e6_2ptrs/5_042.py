__author__ = 'wangqc'

# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height):
        N, water = len(height), 0
        i, j, maxi, maxj = 0, N-1, 0, 0
        while i < j:
            hi, hj = height[i], height[j]
            if hi < hj:
                if hi < maxi:
                    water += maxi-hi
                else:
                    maxi = hi
                i += 1
            else:
                if hj < maxj:
                    water += maxj-hj
                else:
                    maxj = hj
                j -= 1
        return water


if __name__ == '__main__':
    sol = Solution()

    t1 = [0,1,0,2,1,0,1,3,2,1,2,1],
    print(sol.trap(*t1))