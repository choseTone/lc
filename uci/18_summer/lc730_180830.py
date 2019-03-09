__author__ = 'wangqc'

'''
730. Count Different Palindromic Subsequences
Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.
A subsequence of a string S is obtained by deleting 0 or more characters from S.
A sequence is palindromic if it is equal to the sequence reversed.
Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input: 
S = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:
Input: 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation: 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

Note:
The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
'''


class Solution:
    def countPalindromicSubsequences(self, S):
        def cache(start, end):
            if end <= start + 2:
                return end - start
            if (start, end) not in check:
                check[(start, end)] = dfs(start, end)
            return check[(start, end)]

        def dfs(start, end):
            count, seg = 0, S[start: end]
            for x in 'abcd':
                if x in seg:
                    i, j = seg.index(x) + start, seg.rindex(x) + start
                else:
                    continue
                count += cache(i+1, j) + 2 if i != j else 1
            return count % (10**9 + 7)
        check = {}
        return cache(0, len(S))


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

