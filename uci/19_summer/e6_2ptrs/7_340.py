__author__ = 'wangqc'

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        i = j = sub_len = 0
        N, idx = len(s), {}
        while j < N:
            idx[s[j]] = j
            j += 1
            if len(idx) > k:
                evict = min(idx.values())
                idx.pop(s[evict])
                i = evict + 1
            sub_len = max(sub_len, j-i)
        return sub_len


if __name__ == '__main__':
    sol = Solution()

    t1 = "eceba", 2,
    print(sol.lengthOfLongestSubstringKDistinct(*t1))

    t2 = "aa", 1,
    print(sol.lengthOfLongestSubstringKDistinct(*t2))