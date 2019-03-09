__author__ = 'wangqc'

'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        # each valid n pairs string is left + ( + right + ), there are n - 1 valid pairs in left and right combined
        # not include left + ( + ) + right and ( + left + ) + right to avoid repeat counting
        if not n: return ['']
        return [left + '(' + right + ')' for i in range(n)
                for left in self.generateParenthesis(i)
                for right in self.generateParenthesis(n - i - 1)]


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.generateParenthesis(3)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))