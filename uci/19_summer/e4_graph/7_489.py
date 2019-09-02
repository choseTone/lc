__author__ = 'wangqc'

# https://leetcode.com/problems/robot-room-cleaner/

class Robot:
   def move(self):
       pass

   def turnLeft(self):
       pass

   def turnRight(self):
       pass

   def clean(self):
       pass


class Solution:
    def cleanRoom(self, robot):
        D, cleaned = ((-1,0),(0,1),(1,0),(0,-1)), set()
        def dfs(i, j, d):
            robot.clean()
            cleaned.add((i,j))
            left = True
            # move left once then right three times to cover all directions and return back
            for nd in ((d+k)%4 for k in (3,0,1,2)):
                robot.turnLeft() if left else robot.turnRight()
                ni, nj = i+D[nd][0], j+D[nd][1]
                if (ni, nj) not in cleaned and robot.move():
                    dfs(ni, nj, nd)
                    robot.move()    # move back with reversed direction
                    left = True     # direction reversed so move left instead of right
                else:
                    left = False
        dfs(0, 0, 0)





if __name__ == '__main__':
    sol = Solution()

    # skip test here
    # https://leetcode.com/problems/robot-room-cleaner/discuss/270456/Python-Neat-DFS