__author__ = 'wangqc'

'''
647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
'''


class Solution:
    def countSubstrings(self, s):
        s = '$#%s#@' % '#'.join(s)
        n = len(s)
        p, r, c = [0] * n, 0, 0
        for i in range(1, n-1):
            if i < r:
                p[i] = min(r-i, p[2*c-i])
            while s[i+p[i]+1] == s[i-p[i]-1]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]
        return sum((v+1)>>1 for v in p)


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.countSubstrings("abcbahabcba")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

