__author__ = 'wangqc'

# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        i, j, max_len, N = 0, -1, 0, len(s)
        for k in range(1, N):
            if s[k] != s[k-1]:
                if j > -1 and s[j] != s[k]:
                    i, k = j+1, max(max_len, k-i)
                j = k-1
        return max(max_len, N-i)



if __name__ == '__main__':
    sol = Solution()

    t1 = "eceba",
    print(sol.lengthOfLongestSubstringTwoDistinct(*t1))

    t2 = "ccaabbb",
    print(sol.lengthOfLongestSubstringTwoDistinct(*t2))