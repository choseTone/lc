__author__ = 'wangqc'

# https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/269475/Python-BFS-from-Buildings

class Robot:
	def move(self):
		pass

	def turnLeft(self):
		pass

	def turnRight(self):
		pass

	def clean(self):
		pass

def cleanRoom(robot):
	def dfs(robot, i, j, d, cleaned):
		robot.clean()
		cleaned.add((i,j))
		left = True
		for nd in ((d+k) % 4 for k in (3,0,1,2)):
			robot.turnLeft() if left else robot.turnRight()
			di, dj = ((-1,0),(0,-1),(1,0),(0,1))[nd]
			if (i+di, j+dj) not in cleaned and robot.move():
				dfs(robot, i+di, j+dj, nd, cleaned)
				robot.move()
				left = True
			else:
				left = False
	dfs(robot, 0, 0, 0, set())