__author__ = 'wangqc'

'''
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        if not intervals: return []
        intervals = sorted(intervals, key=lambda x: x.start)
        ans = [intervals[0]]
        for i in intervals[1:]:
            if ans[-1].end < i.start: ans.append(i)
            else: ans[-1].end = max(ans[-1].end, i.end)
        return ans


if __name__ == '__main__':
    from time import time

    def list2interval(intervals):
        return [Interval(i[0], i[1]) for i in intervals]

    def interval2list(intervals):
        return[[i.start, i.end] for i in intervals]

    sol = Solution()
    t = time()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    ans = interval2list(sol.merge(list2interval(intervals)))
    print('intervals: %s\nans: %s\ntime: %.3fms' % (intervals, ans, ((time() - t)) * 1000))