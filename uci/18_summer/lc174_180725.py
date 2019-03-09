__author__ = 'wangqc'

'''
174. Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon 
consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and 
must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or 
below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other 
rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path 
RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K)   -3      3
-5      -10	    1
10	    30     -5(P)
 
Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        hp = [[0] * n for _ in range(m)]
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                curr_hp = min(hp[i+1][j], hp[i][j+1]) if i != m-1 and j != n-1 \
                    else hp[m-1][j+1] if j != n-1 else hp[i+1][n-1] if i != m-1 else 1
                hp[i][j] = max(1, curr_hp - dungeon[i][j])
        return hp[0][0]



if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    t = time()

    dungeon = [[randint(-100, 100) for _ in range(100)] for _ in range(100)]
    ans = sol.calculateMinimumHP(dungeon)
    print('dungeon: %s\nans: %s\ntime: %.3fms' % (dungeon, ans, ((time() - t)) * 1000))
