__author__ = 'wangqc'

# https://leetcode.com/problems/longest-turbulent-subarray/


class Solution:
    def maxTurbulenceSize(self, A):
        N = len(A)
        if N == 1:
            return 1
        max_len = curr_len = 1 + (A[0]!=A[1])
        for i in range(1, N-1):
            turb = (A[i-1]-A[i]) * (A[i]-A[i+1])
            if turb < 0:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1 + (A[i] != A[i+1])
        return max(max_len, curr_len)


if __name__ == '__main__':
    sol = Solution()

    t1 = [9,4,2,10,7,8,8,1,9],
    print(sol.maxTurbulenceSize(*t1))

    t2 = [0,8,45,88,48,68,28,55,17,24],
    print(sol.maxTurbulenceSize(*t2))

    t3 = [100],
    print(sol.maxTurbulenceSize(*t3))