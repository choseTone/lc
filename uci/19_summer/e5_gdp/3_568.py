__author__ = 'wangqc'

# https://leetcode.com/problems/maximum-vacation-days/


class Solution:
    def maxVacationDays(self, flights, days):
        # dp[k][i] = days[i][k] + max(dp[k+1][j] for j in graph[i]), city_idx: i,j, week_idx: k
        N, K = len(days), len(days[0])
        graph = {i: {i}|set(j for j in range(N) if flights[i][j]) for i in range(N)}
        curr = [0] * N
        for k in range(K-1, -1, -1):
            prev, curr = curr, [0]* N
            for i in range(N):
                curr[i] = days[i][k] + max(prev[j] for j in graph[i])
        return max(curr[j] for j in graph[0])


if __name__ == '__main__':
    sol = Solution()

    t1 = [[0,1,1],[1,0,1],[1,1,0]], [[1,3,1],[6,0,3],[3,3,3]],
    print(sol.maxVacationDays(*t1))

    t2 = [[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[7,7,7],[7,7,7]],
    print(sol.maxVacationDays(*t2))

    t3 = [[0,1,1],[1,0,1],[1,1,0]], [[7,0,0],[0,7,0],[0,0,7]],
    print(sol.maxVacationDays(*t3))