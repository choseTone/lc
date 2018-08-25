__author__ = 'wangqc'

'''
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
'''


class Solution:
    def removeInvalidParentheses(self, s):
        def remove(s, si, sj, pattern):
            valid = 0
            for i in range(si, len(s)):
                if s[i] == pattern[0]: valid += 1
                if s[i] == pattern[1]: valid -=1
                if valid >= 0: continue
                for j in range(sj, i+1):
                    if s[j] == pattern[1] and (j == sj or s[j-1] != pattern[1]):
                        remove(s[:j]+s[j+1:], i, j, pattern)
                return
            s = s[::-1]
            if pattern[0] == '(':
                remove(s, 0, 0, ')(')
            else:
                ans.append(s)
        ans = []
        remove(s, 0, 0, '()')
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.removeInvalidParentheses("(a)())()")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

