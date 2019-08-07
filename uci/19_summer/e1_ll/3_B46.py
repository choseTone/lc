__author__ = 'wangqc'
# https://leetcode.com/problems/snapshot-array/

import bisect


class SnapshotArray(object):

    def __init__(self, length):
        self.timer = 0
        self.A = [[(0,0)] for _ in range(length)]

    def set(self, index, val):
        self.A[index].append((self.timer, val))

    def snap(self):
        self.timer += 1
        return self.timer - 1

    # binary search
    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], (snap_id+1,))
        return self.A[index][i-1][1]


if __name__ == '__main__':

    obj = SnapshotArray(4)
    print(obj.snap())
    print(obj.snap())
    print(obj.get(3,1))
    print(obj.set(2,4))
    print(obj.snap())
    print(obj.set(1,4))
    print(obj.get(1,2))
    print(obj.get(1,3))

    print()

    obj = SnapshotArray(3)
    print(obj.set(0,5))
    print(obj.snap())
    print(obj.set(0,6))
    print(obj.get(0,0))

