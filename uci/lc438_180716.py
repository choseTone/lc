__author__ = 'wangqc'

'''
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''


class Solution:
    def findAnagrams(self, s, p):
        len_s, len_p, ans  = len(s), len(p), []
        if not p or not s or len_p > len_s: return ans
        counter = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
        for i, c in enumerate(p):
            counter[c] -= 1
            counter[s[i]] += 1
        if not any(counter.values()): ans.append(0)
        for i, c in enumerate(s[len_p:]):
            counter[c] += 1
            counter[s[i]] -= 1
            if not any(counter.values()): ans.append(i+1)
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.findAnagrams("baa", "aa")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
