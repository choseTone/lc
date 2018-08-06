__author__ = 'wangqc'

'''
354. Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into 
another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''

import bisect

class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes_h, dolls = [env[1] for env in sorted(envelopes, key=lambda x: (x[0], -x[1]))], []
        for env_h in envelopes_h:
            i = bisect.bisect_left(dolls, env_h)
            if i >= len(dolls): dolls.append(env_h)
            else: dolls[i] = env_h
        return len(dolls)


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
