__author__ = 'wangqc'


# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights, D):
        S, N = sum(weights), len(weights)
        lo, hi = max(max(weights), S//D), S//D << 1

        def capable(k):
            cnt, load = 1, 0
            for w in weights:
                if load + w > k:
                    cnt, load, = cnt + 1, 0
                    if cnt > D:
                        return False
                load += w
            return True

        while lo < hi:
            mid = lo + hi >> 1
            if capable(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    sol = Solution()

    t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5,
    print(sol.shipWithinDays(*t1))

    t2 = [3, 2, 2, 4, 1, 4], 3,
    print(sol.shipWithinDays(*t2))

    t3 = [1, 2, 3, 1, 1], 4,
    print(sol.shipWithinDays(*t3))
