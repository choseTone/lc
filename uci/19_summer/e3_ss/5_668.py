__author__ = 'wangqc'


# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/


class Solution:
    def findKthNumber(self, m, n, k):
        lo, hi = 1, m*n
        if m > n:
            m, n = n, m

        def less(x):
            cnt = 0
            for r in range(1, min(x,m)+1):
                cnt += min(x//r, n)
                if cnt >= k:
                    return False
            return True

        while lo < hi:
            mid = lo + hi >> 1
            if less(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    sol = Solution()

    t1 = 3, 3, 5,
    print(sol.findKthNumber(*t1))

    t2 = 34, 42, 401,
    print(sol.findKthNumber(*t2))
