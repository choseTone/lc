__author__ = 'wangqc'

# https://leetcode.com/problems/grid-illumination/


from collections import Counter

class Solution:
    def gridIllumination(self, N, lamps, queries):
        lamps_on, lights = set(), [Counter() for _ in range(4)]
        for i, j in lamps:
            lamps_on.add((i, j))
            for k, p in enumerate((i, j, i+j, i-j)):
                lights[k][p] += 1
        ret = []
        for i, j in queries:
            ret.append(int(any(lights[k][p] for k, p in enumerate((i, j, i+j, i-j)))))
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < N and 0 <= y < N and (x,y) in lamps_on:
                    lamps_on.remove((x,y))
                    for k, p in enumerate((x, y, x+y, x-y)):
                        lights[k][p] -= 1
        return ret


if __name__ == '__main__':
    sol = Solution()

    t1 = 5, [[0,0],[4,4]], [[1,1],[1,0]],
    print(sol.gridIllumination(*t1))