__author__ = 'wangqc'


# https://leetcode.com/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, IP):
        segs4, segs6 = IP.split("."), IP.split(":")
        return "IPv4" if len(segs4) == 4 and all(map(self.valid4, segs4)) \
            else "IPv6" if len(segs6) == 8 and all(map(self.valid6, segs6)) \
            else "Neither"

    def valid4(self, seg):
        return seg.isdigit() and 0 <= int(seg) < 256 and (int(seg[0]) or len(seg) == 1)

    def valid6(self, seg):
        return 0 < len(seg) <= 4 and all(map(lambda c: c in "0123456789abcdefABCDEF", seg))


if __name__ == '__main__':
    sol = Solution()

    t1 = "172.16.254.1",
    print(sol.validIPAddress(*t1))

    t2 = "2001:0db8:85a3:0:0:8A2E:0370:7334",
    print(sol.validIPAddress(*t2))

    t3 = "256.256.256.256",
    print(sol.validIPAddress(*t3))
