__author__ = 'wangqc'

# https://leetcode.com/problems/perfect-squares/


class Solution:
    def numSquaresDP(self, n):
        dp = [0]
        for i in range(1, n+1):
            dp.append(min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1)
        return dp[n]

    # BFS works much better here as n can be very large
    def numSquaresBFS(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        cnt, q, nq = 1, {n}, set()
        while q:
            for x in q:
                for square in squares:
                    if x == square:
                        return cnt
                    if x < square:
                        break
                    nq.add(x-square)
            cnt, q, nq = cnt+1, nq, set()


if __name__ == '__main__':
    sol = Solution()

    t1 = 12,
    print(sol.numSquaresDP(*t1))

    t2 = 2007,
    print(sol.numSquaresDP(*t2))