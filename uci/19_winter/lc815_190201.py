__author__ = 'wangqc'

'''
815. Bus Routes

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if 
routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.
We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is 
the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Note:
1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.
'''


class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0
        routes, n = [set(r) for r in routes], len(routes)
        # convert to a graph, node is bus route, edge if two routes intersect
        g = [set() for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if routes[i] & routes[j]: g[i].add(j), g[j].add(i)  # two routes intersect
        seen, dest = set(i for i,r in enumerate(routes) if S in r), set(i for i,r in enumerate(routes) if T in r)
        # use bfs to get the smallest number of bus routes taken
        q = [(node, 1) for node in seen]
        for node, d in q:
            if node in dest: return d
            for nei in g[node]:
                if nei not in seen: seen.add(nei), q.append((nei, d+1))
        return -1


if __name__ == '__main__':
    sol = Solution()
    argv = [[1, 2, 7], [3, 6, 7]], 1, 6
    ans = sol.numBusesToDestination(*argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

