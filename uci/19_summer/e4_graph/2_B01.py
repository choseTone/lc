__author__ = 'wangqc'

# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class Solution:
    def earliestAcq(self, logs, N):
        # g stands for the number of groups that haven't been merged to the big union
        p, sz, g = list(range(N)), [0]*N, N - 1

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if sz[px] < sz[py]:
                    px, py = py, px
                p[py], sz[px] = px, sz[px]+1
                return False
            return True

        for ts, a, b in sorted(logs):
            g -= not union(a, b)
            if not g:
                return ts
        return -1




if __name__ == '__main__':
    sol = Solution()

    t1 = [
             [20190101,0,1],
             [20190104,3,4],
             [20190107,2,3],
             [20190211,1,5],
             [20190224,2,4],
             [20190301,0,3],
             [20190312,1,2],
             [20190322,4,5]
         ], 6
    print(sol.earliestAcq(*t1))