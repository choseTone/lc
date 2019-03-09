__author__ = 'wangqc'

'''
680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''


class Solution:
    def validPalindrome(self, s):
        l, r, _ = self.shrink(s, 0, len(s)-1)
        return self.shrink(s, l+1, r)[2] or self.shrink(s, l, r-1)[2]

    def shrink(self, s, l, r):
        while l < r:
            if s[l] != s[r]: return l, r, False
            l, r = l + 1, r - 1
        return l, r, True


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.validPalindrome("abcdca")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

