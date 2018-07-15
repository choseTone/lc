__author__ = 'wangqc'

'''
310. Minimum Height Trees

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted
tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a
graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected
edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as 
[1, 0] and thus will not appear together in edges.

Example 1 :
Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]

Example 2 :
Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''

import collections


class Solution:
    # shrink from outer to inner; outer node only has one neighbor and shrink means remove outer node for each loop
    # node left at last will be the core node or root of an MHT
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        neighbor = collections.defaultdict(set)
        for v, w in edges:
            neighbor[v].add(w)
            neighbor[w].add(v)
        outers = [i for i in neighbor if len(neighbor[i]) == 1]
        while n > 2:
            n -= len(outers)
            next_outers = []
            for outer in outers:
                next_outer = neighbor[outer].pop()
                neighbor[next_outer].remove(outer)
                if len(neighbor[next_outer]) == 1:
                    next_outers.append(next_outer)
            outers = next_outers
        return outers


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
