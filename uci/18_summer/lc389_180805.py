__author__ = 'wangqc'

'''
389. Find the Difference

Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.

Example:
Input:
s = "abcd"
t = "abcde"
Output:
e
Explanation:
'e' is the letter that was added.
'''


class Solution:
    def findTheDifference(self, s, t):
        ans = 0
        for c in (s+t):
            ans ^= ord(c)
        return chr(ans)


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.findTheDifference("abcd", "abcde")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
