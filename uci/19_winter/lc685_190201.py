__author__ = 'wangqc'

'''
685. Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other 
nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), 
with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not 
an edge that already existed.
The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed 
edge connecting nodes u and v, where u is a parent of child v.
Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, 
return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3

Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3

Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
'''


class Solution:
    def findRedundantDirectedConnection(self, edges):
        # case 1: two parents no cycle, return [any parent, child]
        # case 2: two parents with cycle, return [parent in cycle, child]
        # case 3: one parent with cycle, return any edge
        def find(x):
            if p[x] != x: p[x] = find(p[x])
            return p[x]
        n, p1, p2, c = len(edges), None, None, None
        p = [0] * (n+1)
        for i, (u, v) in enumerate(edges):
            # test for removing [p2, c], correct(case 1 or 2) if not found cycle later
            if p[v]: p1, p2, c, edges[i][0] = p[v], u, v, 0
            else: p[v] = u
        p = list(range(n+1))
        for u, v in edges:
            if u:
                pu, pv = find(u), find(v)
                # if p1 case 2; else case 3
                if pu == pv: return p1 and [p1, c] or [u, v]
                else: p[pv] = pu
        return [p2, c]  # case 1 or 2


if __name__ == '__main__':
    sol = Solution()
    argv = [[1,2], [2,3], [3,4], [4,1], [1,5]]
    ans = sol.findRedundantDirectedConnection(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

