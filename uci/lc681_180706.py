__author__ = 'wangqc'

'''
681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no 
limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are 
all invalid.

Example 1:
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 
19:33, because this occurs 23 hours and 59 minutes later.
 

Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time 
is next day‘s time since it is smaller than the input time numerically.
'''

class Solution:
    def nextClosestTime(self, time):
        # iterate all possible combinations of time digits and pick the one with smallest positive gap (none zero)
        cur = list(map(int, time[:2]+time[3:]))
        choices = [[a, b, c, d] for a in cur for b in cur if a*10+b < 25 for c in cur for d in cur if c*10+d < 60]

        def diff(p):
            cp, cq = map(lambda x: x[0]*600 + x[1]*60 + x[2]*10 + x[3], (p, cur))
            return (cp - cq - 1) % 1441
        closest = min(choices, key=diff)
        return '%d%d:%d%d' % (closest[0], closest[1], closest[2], closest[3])


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.nextClosestTime('01:01')
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
