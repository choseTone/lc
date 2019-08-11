__author__ = 'wangqc'


# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s):
        return [f"{s[:a]}.{s[a:a+b]}.{s[a+b:a+b+c]}.{s[a+b+c:]}"
                for a in range(1, 4) if int(s[:a]) < 256 and (a == 1 or int(s[0]))
                for b in range(1, 4)
                for c in range(1, 4)
                for d in range(1, 4)
                if a + b + c + d == len(s)
                if int(s[a:a + b]) < 256 and (b == 1 or int(s[a]))
                if int(s[a + b:a + b + c]) < 256 and (c == 1 or int(s[a + b]))
                if int(s[a + b + c:]) < 256 and (d == 1 or int(s[a + b + c]))
                ] if len(s) > 3 else []


if __name__ == '__main__':
    sol = Solution()

    t1 = "25525511135",
    print(sol.restoreIpAddresses(*t1))
