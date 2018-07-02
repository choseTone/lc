__author__ = 'wangqc'

import time

'''
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        # using stack; store brackets in a hash map inspired by @ethansure
        # https://github.com/ethansure/Leetcode/blob/master/E20-valid-parentheses.py
        stack, brackets = [], {'{': '}', '[': ']', '(': ')'}
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            elif not stack or i != brackets[stack.pop()]:
                return False
        return not stack


if __name__ == '__main__':
    sol = Solution()
    t = time.time()
    ans = sol.isValid('{[]}()')
    print('ans: %s\ntime: %.2fms' % (ans, ((time.time() - t)) * 1000))