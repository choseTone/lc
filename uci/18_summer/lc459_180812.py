__author__ = 'wangqc'

'''
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the
substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class Solution:
    def repeatedSubstringPattern(self, s):
        return s in (s + s)[1:-1]



if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.repeatedSubstringPattern("abcbcabcabc")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

