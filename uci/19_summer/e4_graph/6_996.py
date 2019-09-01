__author__ = 'wangqc'

# https://leetcode.com/problems/number-of-squareful-arrays/


from collections import Counter

class Solution:
    def numSquarefulPerms(self, A):
        pool, self.cnt = Counter(A), 0
        graph = {i: {j for j in pool if int((i+j)**0.5)==(i+j)**0.5} for i in pool}

        def dfs(node, undo):
            pool[node] -= 1
            for nei in graph[node]:
                if pool[nei]:
                    if undo:
                        dfs(nei, undo-1)
                    else:
                        self.cnt += 1
            pool[node] += 1

        for node in pool:
            dfs(node, len(A)-2)
        return self.cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,17,8],
    print(sol.numSquarefulPerms(*t1))

    t2 = [2,2,2],
    print(sol.numSquarefulPerms(*t2))