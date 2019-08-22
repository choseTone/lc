__author__ = 'wangqc'


# https://leetcode.com/problems/super-egg-drop/solution/


import time

class Solution:
    def superEggDropDP(self, K, N):
        dp, i = [list(range(N+1)), [0]*(N+1)], 0

        def opt(x):
            return max(dp[1-i][x-1], dp[i][n-x])

        for _ in range(K-1):
            i, x = 1-i, 1
            for n in range(1, N+1):
                while x < n and opt(x) > opt(x+1):
                    x += 1
                dp[i][n] = 1 + opt(x)
        return dp[K+1&1][-1]

    def superEggDropMath(self, K, N):
        def f(x):
            cnt, c, i = 0, 1, 1
            while cnt < N and i < K+1:
                c = c * (x-i+1) // i
                cnt += c
                i += 1
            return cnt

        lo, hi = 1, N
        while lo < hi:
            mid = lo + hi >> 1
            if f(mid) < N:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    sol = Solution()

    t1 = 100, 8192,
    t = time.time()
    print(sol.superEggDropDP(*t1), time.time()-t)

    t = time.time()
    print(sol.superEggDropMath(*t1), time.time() - t)
