__author__ = 'wangqc'

# https://leetcode.com/problems/sum-of-distances-in-tree/discuss/256963/Python-DFS
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sumOfDistancesInTree(N, edges):
    graph = collections.defaultdict(set)
    for u, v in edges: graph[u].add(v), graph[v].add(u)
    count, dist = [1] * N, [0] * N

    def dfs(node, parent):
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                count[node] += count[child]
                dist[node] += dist[child] + count[child]

    def dfs_final(node, parent):
        for child in graph[node]:
            if child != parent:
                dist[child] = dist[node] - count[child] + (N - count[child])
                dfs_final(child, node)

    dfs(0, None), dfs_final(0, None)
    return dist