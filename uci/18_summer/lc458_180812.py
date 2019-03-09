__author__ = 'wangqc'

'''
458. Poor Pigs

There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. 
If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out 
which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:
If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the 
"poison" bucket within p minutes? There is exact one bucket with poison.
'''

import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        return math.ceil(math.log(buckets, (1 + minutesToTest / minutesToDie)))


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.poorPigs(1000, 15, 60)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

