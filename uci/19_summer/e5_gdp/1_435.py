__author__ = 'wangqc'

# https://leetcode.com/problems/non-overlapping-intervals/


class Solution:
    def eraseOverlapIntervals(self, intervals):
        cnt, bound = 0, float('-inf')
        for s, e in sorted(intervals, key=lambda x:x[1]):
            if s < bound:
                cnt += 1
            else:
                bound = e
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,2],[2,3],[3,4],[-100,-2],[5,7]],
    print(sol.eraseOverlapIntervals(*t1))

    t2 = [[1,2],[1,2],[1,2]],
    print(sol.eraseOverlapIntervals(*t2))

    t3 = [[1,2],[2,3]],
    print(sol.eraseOverlapIntervals(*t3))