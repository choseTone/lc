__author__ = 'wangqc'

'''
854. K-Similar Strings

Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A 
exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:
Input: A = "ab", B = "ba"
Output: 1

Example 2:
Input: A = "abc", B = "bca"
Output: 2

Example 3:
Input: A = "abac", B = "baca"
Output: 2

Example 4:
Input: A = "aabc", B = "abca"
Output: 2
'''


class Solution:
    def kSimilarity(self, A, B):
        # neighbor string is one sway away with the left-most unmatched character
        def neighbors(s):
            for i, c in enumerate(s):
                if c != B[i]: break
            for j in range(i+1, len(s)):
                if s[j] == B[i]: yield s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
        q, seen = [A], {A: 0}
        for node in q:
            if node == B: return seen[node]
            for nei in neighbors(node):
                if nei not in seen:
                    seen[nei] = seen[node] + 1
                    q.append(nei)


if __name__ == '__main__':
    sol = Solution()
    argv = "abac", "baca"
    ans = sol.kSimilarity(*argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

