__author__ = 'wangqc'

'''
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


class Solution:
    def firstUniqChar(self, s):
        uniques = [s.index(c) for c in 'abcdefghijklmnopqrstuvwxyz' if s.count(c) == 1]
        return min(uniques) if uniques else -1


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.firstUniqChar("loveleetcode")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
