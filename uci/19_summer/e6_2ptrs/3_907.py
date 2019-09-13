__author__ = 'wangqc'

# https://leetcode.com/problems/sum-of-subarray-minimums/


class Solution:
    def sumSubarrayMins(self, A):
        stack, A, cnt, M = [0], [0]+A+[0], 0, 10**9+7
        for k, x in enumerate(A[1:], 1):
            while x < A[stack[-1]]:
                j, i = stack.pop(), stack[-1]
                cnt = (cnt + A[j]*(k-j)*(j-i)) % M
            stack.append(k)
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [3,1,2,4],
    print(sol.sumSubarrayMins(*t1))

    t2 = [94,9,31,8,105],
    print(sol.sumSubarrayMins(*t2))