__author__ = 'wangqc'

'''
316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only
once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: "bcabc"
Output: "abc"

Example 2:
Input: "cbacdcbc"
Output: "acdb"
'''


class Solution:
    def removeDuplicateLetters(self, s):
        chars, ans = {c: i for i, c in enumerate(s)}, ''
        for i, c in enumerate(s):
            if c not in ans:
                # i < chars[ans[-1]] indicates there is another ans[-1] character in the later string
                while ans and c < ans[-1] and i < chars[ans[-1]]:
                    ans = ans[:-1]
                ans += c
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.removeDuplicateLetters("abacb")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
