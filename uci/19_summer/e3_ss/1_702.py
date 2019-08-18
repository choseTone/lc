__author__ = 'wangqc'
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/


class ArrayReader:
    def __init__(self, A):
        self.A = A
        self.N = len(A)

    def get(self, i):
        return self.A[i] if i < self.N else float('inf')

class Solution:
    def search(self, reader, target):
        hi = 1
        while reader.get(hi) < target:
            hi <<= 1
        lo = hi >> 1
        while lo <= hi:
            mid = lo + hi >> 1
            if reader.get(mid) < target:
                lo = mid+1
            elif reader.get(mid) > target:
                hi = mid - 1
            else:
                return mid
        return -1



if __name__ == '__main__':
    sol = Solution()

    t1 = ArrayReader([-1,0,3,5,9,12]), 9
    print(sol.search(*t1))

    t1 = ArrayReader([-1,0,3,5,9,12]), 2
    print(sol.search(*t1))
