__author__ = 'wangqc'

'''
657. Judge Route Circle

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, 
which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are 
R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
'''


class Solution:
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.judgeCircle("UD")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))