__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/


from collections import deque


class Solution:
    def shortestSubarray(self, A, K):
        agg, N = 0, len(A)
        min_len = N + 1
        q = deque([(-1, 0)])
        for i, x in enumerate(A):
            agg += x
            while q and agg - q[0][1] >= K:
                min_len = min(min_len, i-q.popleft()[0])
            while q and agg <= q[-1][1]:
                q.pop()
            q.append((i, agg))
        return min_len if min_len < N + 1 else -1


if __name__ == '__main__':
    sol = Solution()

    t1 = [1], 1,
    print(sol.shortestSubarray(*t1))

    t2 = [56,-21,56,35,-9], 61,
    print(sol.shortestSubarray(*t2))

    t3 = [84,-37,32,40,95], 167,
    print(sol.shortestSubarray(*t3))