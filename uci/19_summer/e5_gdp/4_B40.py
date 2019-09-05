__author__ = 'wangqc'

# https://leetcode.com/problems/stone-game-ii/


from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        N = len(piles)
        for i in range(N-2, -1, -1):
            piles[i] += piles[i+1]

        @lru_cache(None)
        # currently pick from piles[i:], M=m, pick x piles to make opponent get minimum stones
        def dp(i, m):
            if i + (m<<1) >= N:
                return piles[i]
            return piles[i] - min(dp(i+x, max(x,m)) for x in range(1, (m<<1)+1))

        return dp(0, 1)


if __name__ == '__main__':
    sol = Solution()

    t1 = [2,7,9,4,4],
    print(sol.stoneGameII(*t1))

    t2 = [1473,9520,4041,7800,1586,8502,333,7993,3843,7636,9455,4460,6447,496,3874,6239,6108,3142,5429,9366,5743,8785,
          7301,2118,852,7907,5431,5010,6889,2419,6221,2913,6181,1589,8471,8789,2222,8518,9990,8271,3851,6730,7344,8151,
          6620,6873,6533,7144,8761,9146,6965,4686,3275,5015,7162,8183,1664,427,5519,5852],
    print(sol.stoneGameII(*t2))