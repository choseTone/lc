__author__ = 'wangqc'
# https://leetcode.com/problems/pancake-sorting/


class Solution:
    def pancakeSort(self, A):
        flips, N = [], len(A)
        for k in range(N, 1, -1):
            i = A.index(k)
            if i < k-1:
                flips += [i+1, k] if i else [k]
            A = A[:i:-1] + A[:i]
        return flips


if __name__ == '__main__':
    sol = Solution()

    t1 = [3,2,4,1],
    print(sol.pancakeSort(*t1))

    t1 = [1,2,3],
    print(sol.pancakeSort(*t1))
