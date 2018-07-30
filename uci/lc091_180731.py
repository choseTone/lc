__author__ = 'wangqc'

'''
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


class Solution:
    def numDecodings(self, s):
        ans, prev_ans, prev = int(s > ''), 0, ''
        for curr in s:
            prev_ans, ans, prev = ans, ans * (curr > '0') + prev_ans * (0 < int(prev + curr) < 27), curr
        return ans



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.numDecodings("2267")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
