__author__ = 'wangqc'


# https://leetcode.com/problems/find-peak-element/

class MountainArray:
    def __init__(self, A):
        self.A = A

    def get(self, i):
        return self.A[i]

    def length(self):
        return len(self.A)


class Solution:
    def findInMountainArray(self, A, target):
        l, r = 0, A.length() - 1
        while l < r:
            m = l + r >> 1
            if A.get(m) > A.get(m + 1):
                r = m
            else:
                l = m + 1

        def bisearch(l, r, sign):
            while l <= r:
                m = l + r >> 1
                if A.get(m) * sign > target * sign:
                    r = m - 1
                elif A.get(m) * sign < target * sign:
                    l = m + 1
                else:
                    return m
            return -1
        x = bisearch(0, l, 1)
        return x if x >= 0 else bisearch(l, A.length() - 1, -1)


if __name__ == '__main__':
    sol = Solution()

    t1 = MountainArray([1, 2, 3, 4, 5, 3, 1]), 3,
    print(sol.findInMountainArray(*t1))

    t1 = MountainArray([0, 1, 2, 4, 2, 1]), 3,
    print(sol.findInMountainArray(*t1))
