__author__ = 'wangqc'

# https://leetcode.com/problems/video-stitching/


class Solution:
    def knightDialer(self, N):
        pad, M = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]], 10**9 + 7
        curr = [1]*10
        for _ in range(N-1):
            prev = curr
            curr = [sum(prev[j] for j in pad[i]) % M for i in range(10)]
        return sum(curr) % M


if __name__ == '__main__':
    sol = Solution()

    t1 = 3,
    print(sol.knightDialer(*t1))

    t2 = 100,
    print(sol.knightDialer(*t2))

    t3 = 666,
    print(sol.knightDialer(*t3))