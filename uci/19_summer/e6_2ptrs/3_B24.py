__author__ = 'wangqc'

# https://leetcode.com/problems/longest-well-performing-interval/


class Solution:
    def longestWPI(self, hours):
        prev, agg, length, N = {}, 0, 0, len(hours)
        for i, hour in enumerate(hours):
            agg += [-1,1][hour > 8]
            prev.setdefault(agg, i)
            if agg > 0:
                length = i + 1
            else:
                length = max(length, i-prev.get(agg-1, N))
        return length


if __name__ == '__main__':
    sol = Solution()

    t1 = [9,9,6,0,6,6,9],
    print(sol.longestWPI(*t1))

    t2 = [9,9,6],
    print(sol.longestWPI(*t2))

    t3 = [6,6,6],
    print(sol.longestWPI(*t3))