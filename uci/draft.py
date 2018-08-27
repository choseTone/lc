__author__ = 'wangqc'


class Solution:
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        def dfs(x, y, stopped):
            if [x, y] == destination: return True
            if (x, y) in stopped: return False
            stopped.add((x, y))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n and not maze[nx][ny]:
                    nx, ny = nx + dx, ny + dy
                if dfs(nx - dx, ny - dy, stopped): return True
            return False
        x, y = start
        return dfs(x, y, set())


print(Solution().hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2]))