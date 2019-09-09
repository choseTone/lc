__author__ = 'wangqc'

# https://leetcode.com/problems/profitable-schemes/


class Solution:
    def longestValidParentheses(self, s):
        stack, length = [-1], 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    length = max(length, i-stack[-1])
                else:
                    stack.append(i)
        return length


if __name__ == '__main__':
    sol = Solution()

    t1 = "(()",
    print(sol.longestValidParentheses(*t1))

    t2 = ")()())",
    print(sol.longestValidParentheses(*t2))