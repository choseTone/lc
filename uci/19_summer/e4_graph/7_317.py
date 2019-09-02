__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-distance-from-all-buildings/


class Solution:
    def shortestDistance(self, grid):
        M, N = len(grid), len(grid[0])
        blds, dists = [[0]*N for _ in range(M)], [[0]*N for _ in range(M)]
        B = sum(1 for i in range(M) for j in range(N) if grid[i][j]==1)

        def bfs(i, j):
            q, seen, cnt = [(i,j,1)], {(i,j)}, 1
            for x, y, d in q:
                for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] < 2 and ((nx, ny)) not in seen:
                        seen.add((nx, ny))
                        if not grid[nx][ny]:
                            blds[nx][ny] += 1
                            dists[nx][ny] += d
                            q.append((nx, ny, d+1))
                        else:
                            cnt += 1
            return cnt == B

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and not bfs(i,j):
                    return -1
        return min((dists[i][j] for i in range(M) for j in range(N) if not grid[i][j] and blds[i][j]==B), default=-1)


if __name__ == '__main__':
    sol = Solution()

    t1 = [
             [1,0,2,0,1],
             [0,0,0,0,0],
             [0,0,1,0,0]
         ],
    print(sol.shortestDistance(*t1))