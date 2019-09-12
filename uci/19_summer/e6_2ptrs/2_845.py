__author__ = 'wangqc'

# https://leetcode.com/problems/longest-mountain-in-array/


class Solution:
    def longestMountain(self, A):
        N = len(A)
        if N < 3:
            return 0
        def up(i):
            return i < N-1 and A[i] < A[i+1]

        def down(i):
            return i < N-1 and A[i] > A[i+1]

        l = r = length = 0
        while l < N - 1:
            if up(r):
                while up(r):
                    r += 1
                if down(r):
                    while down(r):
                        r += 1
                    length = max(length, r-l+1)
            l = r = max(r, l+1)
        return length


if __name__ == '__main__':
    sol = Solution()

    t1 = [2,1,4,7,3,2,5],
    print(sol.longestMountain(*t1))

    t2 = [2,2,2],
    print(sol.longestMountain(*t2))

    t3 = list(range(10)),
    print(sol.longestMountain(*t3))

    t4 = list(range(9,-1,-1)),
    print(sol.longestMountain(*t4))