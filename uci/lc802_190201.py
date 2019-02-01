__author__ = 'wangqc'

'''
802. Find Eventual Safe States

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node 
that is terminal (that is, it has no outgoing directed edges), we stop.
Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, 
there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in 
less than K steps.
Which nodes are eventually safe?  Return them as an array in sorted order.
The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in 
the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Note:
graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
'''

import collections

class Solution:
    def eventualSafeNodes(self, graph):
        color = collections.Counter()
        # color 0, unexplored; color 1, a potential cycle node; color 2, only link to end node
        def dfs(node):  # return true if not a part of cycle
            if color[node]: return color[node] == 2
            color[node] = 1
            for nei in graph[node]:
                if color[nei] == 2: continue
                # nei has been colored to 1 before, so a cycle detected
                if color[nei] == 1 or not dfs(nei): return False
            color[node] = 2 # not a part of cycle, change color to 2
            return True
        return list(filter(dfs, range(len(graph))))


if __name__ == '__main__':
    sol = Solution()
    argv = [[1,2],[2,3],[5],[0],[5],[],[]]
    ans = sol.eventualSafeNodes(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

