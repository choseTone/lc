__author__ = 'wangqc'

'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''


class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower(): return False
            l, r = l + 1, r - 1
        return True


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.isPalindrome("A man, a plan, a canal: Panama")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

