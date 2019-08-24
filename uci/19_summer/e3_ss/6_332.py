__author__ = 'wangqc'


# https://leetcode.com/problems/reconstruct-itinerary/

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph, stack, route = defaultdict(list), ["JFK"], []
        for dst, src in sorted(tickets, reverse=True):
            graph[dst].append(src)
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.insert(0, stack.pop())
        return route

if __name__ == '__main__':
    sol = Solution()

    t1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
    print(sol.findItinerary(*t1))

    t2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
    print(sol.findItinerary(*t2))
