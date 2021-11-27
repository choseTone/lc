__author__ = 'wangqc'

# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/


class Solution:
    def maximumSum(self, arr):
        n = len(arr)
        fwd, bwd = [0] * n, [0] * n
        ans, s = arr[0], 0
        for i, x in enumerate(arr):
            fwd[i] = (s := max(x, s+x))
            ans = max(ans, s)
        s = 0
        for i, x in enumerate(arr[::-1]):
            bwd[n-i-1] = (s := max(x, s+x))
        for i in range(1, n-1):
            ans = max(ans, fwd[i-1]+bwd[i+1])  # subarray that deletes arr[i]
        return ans


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,-2,0,3],
    print(sol.maximumSum(*t1))

    t2 = [-1,-1,-1,-1],
    print(sol.maximumSum(*t2))

    t3 = [-8,7,-12,-1,0,11,-2,-3,4,-13,2,3,-6],
    print(sol.maximumSum(*t3))

    t4 = [1,-10,2,-10,3],
    print(sol.maximumSum(*t4))