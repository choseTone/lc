__author__ = 'wangqc'

'''
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''


class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        l, r, v = 0, len(s)-1, list(s)
        while l < r:
            while l < r and v[l] not in vowels:
                l += 1
            while l < r and v[r] not in vowels:
                r -= 1
            v[l], v[r], = v[r], v[l]
            l, r = l+1, r-1
        return ''.join(v)


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.reverseVowels("leetcode")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
