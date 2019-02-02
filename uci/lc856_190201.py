__author__ = 'wangqc'

'''
856. Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:
() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:
Input: "()"
Output: 1

Example 2:
Input: "(())"
Output: 2

Example 3:
Input: "()()"
Output: 2

Example 4:
Input: "(()(()))"
Output: 6
'''


class Solution:
    def scoreOfParentheses(self, S):
        def dc(i, j):
            bal = ans = 0
            for k in range(i, j):
                bal += 1 if S[k] == "(" else -1
                if not bal:
                    if k == i+1: ans += 1
                    else: ans += 2 * dc(i+1, k)
                    i = k+1
            return ans
        return dc(0, len(S))


if __name__ == '__main__':
    sol = Solution()
    argv = "(()(()))"
    ans = sol.scoreOfParentheses(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

