__author__ = 'wangqc'

'''
864. Shortest Path to Get All Keys

We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are 
keys, and ("A", "B", ...) are locks.
We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  
We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock 
unless we have the corresponding key.
For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English 
alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that 
the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

Example 1:
Input: ["@.a.#","###.#","b.A.B"]
Output: 8

Example 2:
Input: ["@..aA","..B#.","....b"]
Output: 6
 
Note:
1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
'''

import heapq

class Solution:
    # 'k' and 'keys' are binary key chains that each bit corresponds to a key
    # in the graph, each node is a status (used steps, current location, found keys)
    def shortestPathAllKeys(self, grid):
        def atoi(c): return ord(c) - ord('a')
        m, n, keys, si, sj = len(grid), len(grid[0]), 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@': si, sj = i, j
                if grid[i][j].islower(): keys |= 1 << atoi(grid[i][j])  # key chain with all keys
        q, seen = [(0, si, sj, 0)], set()
        while q:
            step, i, j, k = heapq.heappop(q)    # dijkstra, choose node with the smallest weight
            if k == keys: return step    # find all the keys
            for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                    # meet a lock but without the key to open the lock
                    if grid[x][y].isupper() and not k & 1 << atoi(grid[x][y].lower()): continue
                    # find a key, set the bit
                    nk = k | 1 << atoi(grid[x][y]) if grid[x][y].islower() else k
                    if (nk, x, y) not in seen:
                        seen.add((nk, x, y))
                        heapq.heappush(q, (step+1, x, y, nk))
        return -1

if __name__ == '__main__':
    sol = Solution()
    argv = ["@.a.#","###.#","b.A.B"]
    ans = sol.shortestPathAllKeys(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

