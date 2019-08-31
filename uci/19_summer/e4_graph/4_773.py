__author__ = 'wangqc'

# https://leetcode.com/problems/sliding-puzzle/

from collections import defaultdict


class Solution:
    def slidingPuzzle(self, board):
        def move(s, i, j):
            if i > j:
                i, j = j, i
            return s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]

        graph = {0:(1,3), 1:(0,2,4), 2:(1,5), 3:(0,4), 4:(1,3,5), 5:(2,4)}
        state = ''.join(map(str, sum(board, [])))
        seen = {state}
        q = [(state, state.index("0"), 0)]
        for state, x, steps in q:
            if state == "123450":
                return steps
            for y in graph[x]:
                new_state = move(state, x, y)
                if new_state not in seen:
                    q.append((new_state, y, steps+1))
                    seen.add(new_state)
        return -1


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,2,3],[5,4,0]],
    print(sol.slidingPuzzle(*t1))

    t2 = [[4,1,2],[5,0,3]],
    print(sol.slidingPuzzle(*t2))
