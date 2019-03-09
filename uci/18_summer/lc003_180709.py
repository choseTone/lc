__author__ = 'wangqc'

'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a 
subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        ans, start, lookup = 0, -1, {}
        for i, c in enumerate(s):
            if c in lookup and lookup[c] > start:
                start = lookup[c]
            ans, lookup[c] = max(ans, i - start), i
        return ans



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.lengthOfLongestSubstring('theanswermustbeasubstring')
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))