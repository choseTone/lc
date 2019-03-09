__author__ = 'wangqc'

'''
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''


class Solution:
    def calculate(self, s):
        ans, i, n, sign = 0, 0, len(s), [1, 1]
        while i < n:
            if s[i].isdigit():
                j = i
                while i+1 < n and s[i+1].isdigit():
                    i += 1
                ans += int(s[j:i+1]) * sign.pop()
            if s[i] in '(+-)':
                if s[i] == ')': sign.pop()
                else: sign.append(sign[-1] * (1, -1)[s[i] == '-'])
            i += 1
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.calculate("1 + 1")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
