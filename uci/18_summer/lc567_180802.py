__author__ = 'wangqc'

'''
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, 
one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''


class Solution:
    def checkInclusion(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        if l1 > l2: return False
        count = [0] * 26
        for i in range(l1):
            count[ord(s1[i]) - 97] += 1
            count[ord(s2[i]) - 97] -= 1
        if not any(count): return True
        for i in range(l1, l2):
            count[ord(s2[i]) - 97] -= 1
            count[ord(s2[i-l1]) - 97] += 1
            if not any(count): return True
        return False







if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.checkInclusion("ab", "eidbaooo")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
