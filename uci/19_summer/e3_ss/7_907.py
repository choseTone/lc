__author__ = 'wangqc'


# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, A):
        stack, A, cnt, M = [], [0] + A + [0], 0, 10 ** 9 + 7
        for j, x in enumerate(A):
            while stack and A[stack[-1]] > x:
                k, i = stack.pop(), stack[-1]
                cnt = (cnt + A[k]*(j-k)*(k-i)) % M
            stack.append(j)
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [3, 1, 2, 4],
    print(sol.sumSubarrayMins(*t1))
