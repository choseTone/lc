__author__ = 'wangqc'

# https://leetcode.com/problems/loud-and-rich/

from collections import defaultdict


class Solution:
    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        tree, lnr = defaultdict(set), [-1] * N
        for dst, src in richer:
            tree[src].add(dst)

        def dfs(node):
            if lnr[node] < 0:
                lnr[node] = min([dfs(nei) for nei in tree[node]]+[node], key=lambda x:quiet[x])
            return lnr[node]

        return list(map(dfs, range(N)))



if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0],
    print(sol.loudAndRich(*t1))
