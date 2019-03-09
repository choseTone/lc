__author__ = 'wangqc'

'''
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        for c in t:
            if c not in chars or not chars[c]:
                return False
            chars[c] -= 1
        return not any(chars.values())



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.isAnagram('anagram', 'nagaram')
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))