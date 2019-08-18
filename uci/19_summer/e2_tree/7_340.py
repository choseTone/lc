__author__ = 'wangqc'


# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        i = j = l = 0
        N, dp = len(s), {}
        while j < N:
            dp[s[j]] = j
            j += 1
            if len(dp) > k:
                evict = min(dp.values())
                del dp[s[evict]]
                i = evict + 1
            l = max(l, j-i)
        return l


if __name__ == '__main__':
    sol = Solution()

    t1 = "panamabanana", 2,
    print(sol.lengthOfLongestSubstringKDistinct(*t1))

    t2 = "panamabanana", 3,
    print(sol.lengthOfLongestSubstringKDistinct(*t2))
