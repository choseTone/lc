__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-way-to-form-string/


from collections import defaultdict
import bisect

class Solution:
    def shortestWay2P(self, source, target):
        cnt = t = j = 0
        M, N = len(source), len(target)
        while t < N:
            for i in range(M):
                j += source[i] == target[j]
                if j == N: break
            if j == t:
                return -1
            cnt += 1
            t = j
        return cnt

    def shortestWayBS(self, source, target):
        sid = defaultdict(list)
        for i, c in enumerate(source):
            sid[c].append(i)
        i, cnt = -1, 1
        for c in target:
            if c not in sid:
                return -1
            curr_id = sid[c]
            j = bisect.bisect_left(curr_id, i)
            if j == len(curr_id):
                cnt += 1
                i = curr_id[0] + 1
            else:
                i = curr_id[j] + 1
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = "abc", "abcbc",
    print(sol.shortestWay2P(*t1))
    print(sol.shortestWayBS(*t1))

    t2 = "abc", "acdbc",
    print(sol.shortestWay2P(*t2))
    print(sol.shortestWayBS(*t2))

    t3 = "xyz", "xzyxz",
    print(sol.shortestWay2P(*t3))
    print(sol.shortestWayBS(*t3))