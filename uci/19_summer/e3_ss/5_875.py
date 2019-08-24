__author__ = 'wangqc'


# https://leetcode.com/problems/koko-eating-bananas/


class Solution:
    def minEatingSpeed(self, piles, H):
        S, N = sum(piles), len(piles)

        def ceil(x, y):
            return (x - 1) // y + 1

        lo, hi = ceil(S, H), min(max(piles), ceil(S, H-N+1))
        while lo < hi:
            mid = lo + hi >> 1
            if sum(ceil(p, mid) for p in piles) > H:
                lo = mid + 1
            else:
                hi = mid
        return lo



if __name__ == '__main__':
    sol = Solution()

    t1 = [30,11,23,4,20], 5,
    print(sol.minEatingSpeed(*t1))

    t2 = [30,11,23,4,20], 6,
    print(sol.minEatingSpeed(*t2))
