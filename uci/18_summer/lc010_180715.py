__author__ = 'wangqc'

'''
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


class Solution:
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        match = [[False] * (lp+1) for _ in range(ls+1)]
        match[ls][lp] = True
        for i in range(ls+1)[::-1]:
            for j in range(lp)[::-1]:
                curr_match = i < ls and p[j] in {'.', s[i]}
                match[i][j] = match[i][j+2] or curr_match and match[i+1][j] if j+1 < lp and p[j+1] == '*' \
                    else curr_match and match[i+1][j+1]
        return match[0][0]


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.isMatch("mississippi", "mis*is*ip*i")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
