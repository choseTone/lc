__author__ = 'wangqc'

# https://leetcode.com/problems/pacific-atlantic-water-flow/


class Solution:
    def pacificAtlantic(self, matrix):
        M, N = len(matrix), len(matrix) and len(matrix[0])
        flow = [[0]*N for _ in range(M)]

        def bfs(q, ocean):
            for i, j in q:
                flow[i][j] |= ocean
            for i, j in q:
                for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0 <= x < M and 0 <= y < N and not (flow[x][y] & ocean) and matrix[x][y]>=matrix[i][j]:
                        flow[x][y] |= ocean
                        q.append((x,y))

        pacifics = [(i,0) for i in range(M)] + [(0,j) for j in range(N)]
        altantics = [(i,N-1) for i in range(M)] + [(M-1,j) for j in range(N)]
        bfs(pacifics, 1), bfs(altantics, 2)
        return [[i, j] for i in range(M) for j in range(N) if flow[i][j]==3]


if __name__ == '__main__':
    sol = Solution()

    t1 = [
             [1,2,2,3,5],
             [3,2,3,4,4],
             [2,4,5,3,1],
             [6,7,1,4,5],
             [5,1,1,2,4]
         ],
    print(sol.pacificAtlantic(*t1))
