__author__ = 'wangqc'

# https://leetcode.com/problems/online-majority-element-in-subarray/

from collections import defaultdict
import bisect


class MajorityChecker:
    def __init__(self, arr):
        self.time_series = defaultdict(list)
        for time, vote in enumerate(arr):
            self.time_series[vote].append(time)
        self.time_series = sorted(self.time_series.items(), key=lambda x: -len(x[1]))

    def query(self, left, right, threshold):
        for vote, times in self.time_series:
            if len(times) < threshold:
                break
            if bisect.bisect(times, right) - bisect.bisect_left(times, left) >= threshold:
                return vote
        return -1


if __name__ == '__main__':
    obj = MajorityChecker([1,1,2,2,1,1])
    print(obj.query(0,5,4))
    print(obj.query(0,3,3))
    print(obj.query(2,3,2))

