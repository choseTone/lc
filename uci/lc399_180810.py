__author__ = 'wangqc'

'''
399. Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number 
(floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries, 
where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''

import collections

class Solution:
    def calcEquation(self, equations, values, queries):
        record = collections.defaultdict(dict)
        for (n, d), val in zip(equations, values):
            record[n][n] = record[d][d] = 1.0
            record[n][d], record[d][n] = val, 1.0 / val
        for x in record:
            for y in record[x]:
                for z in record[x]:
                    record[y][z] = record[y][x] * record[x][z]
        return [record[n].get(d, -1.0) for n, d in queries]


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
