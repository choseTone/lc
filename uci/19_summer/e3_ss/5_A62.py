__author__ = 'wangqc'


# https://leetcode.com/problems/longest-repeating-substring/


class Solution:
    def longestRepeatingSubstring(self, S):
        N = len(S)

        def exist(k):
            for i in range(N-k+1):
                if S.find(S[i:i+k], i+1) > 0:
                    return True
            return False

        lo, hi = 0, N
        while lo < hi:
            mid = lo + hi >> 1
            if exist(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1




if __name__ == '__main__':
    sol = Solution()

    t1 = "abcd",
    print(sol.longestRepeatingSubstring(*t1))

    t2 = "abbaba",
    print(sol.longestRepeatingSubstring(*t2))

    t3 = "aaabaabbbaaabaabbaabbbabbbaaaabbaaaaaabbbaabbbbbbbbbaaaabbabbaba",
    print(sol.longestRepeatingSubstring(*t3))
