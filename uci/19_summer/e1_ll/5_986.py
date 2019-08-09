__author__ = 'wangqc'
# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, A, B):
        i, j, m, n, intersect = 0, 0, len(A), len(B), []
        while i < m and j < n:
            lo, hi = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
            if lo <= hi:
                intersect.append([lo, hi])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return intersect


if __name__ == '__main__':

    sol = Solution()

    t1 = [[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]],
    print(sol.intervalIntersection(*t1))

