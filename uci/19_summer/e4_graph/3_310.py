__author__ = 'wangqc'

# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict


class Solution:
    def findOrder(self, n, prerequisites):
        src, dst = [set() for _ in range(n)], defaultdict(set)
        for d, s in prerequisites:
            src[d].add(s)
            dst[s].add(d)
        order = [node for node in range(n) if not src[node]]
        for node in order:
            for nei in dst[node]:
                src[nei].remove(node)
                if not src[nei]:
                    order.append(nei)
        return order if len(order) == n else []


if __name__ == '__main__':
    sol = Solution()

    t1 = 2, [[1,0]],
    print(sol.findOrder(*t1))

    t2 = 4, [[1,0],[2,0],[3,1],[3,2]],
    print(sol.findOrder(*t2))