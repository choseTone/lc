__author__ = 'wangqc'

# https://leetcode.com/problems/k-similar-strings/


class Solution:
    def solveNQueens(self, n):
        solutions = []

        def dfs(state, fs, bs):
            row = len(state)
            if row == n:
                solutions.append(state)
            else:
                for col in range(n):
                    if col not in state and col+row not in fs and col-row not in bs:
                        dfs(state+[col], fs|{col+row}, bs|{col-row})

        dfs(list(), set(), set())
        return [["."*c+"Q"+"."*(n-c-1) for c in state] for state in solutions]



if __name__ == '__main__':
    sol = Solution()

    t1 = 4,
    print(sol.solveNQueens(*t1))

    t2 = 8,
    print(sol.solveNQueens(*t2))