__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-height-trees/


class Solution:
    def findMinHeightTrees(self, n, edges):
        tree = [set() for _ in range(n)]
        for u, v in edges:
            tree[u].add(v), tree[v].add(u)
        q, nq = set(x for x in range(n) if len(tree[x]) < 2), set()
        while True:
            for x in q:
                for y in tree[x]:
                    tree[y].remove(x)
                    if len(tree[y]) == 1:
                        nq.add(y)
            if not nq:
                break
            q, nq = nq, set()
        return list(q)



if __name__ == '__main__':
    sol = Solution()

    t1 = 4, [[1, 0], [1, 2], [1, 3]],
    print(sol.findMinHeightTrees(*t1))

    t2 = 6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]],
    print(sol.findMinHeightTrees(*t2))
