__author__ = 'wangqc'

# https://leetcode.com/problems/push-dominoes/


class Solution:
    def pushDominoes(self, dominoes):
        events = [(i, c) for i, c in enumerate(f"L{dominoes}R", -1) if c != "."]
        dominoes = list(dominoes)
        for (i,l), (j,r) in zip(events, events[1:]):
            if l == r:
                dominoes[i+1:j] = [l] * (j-i-1)
            elif l > r:
                m = j-i-1 >> 1
                dominoes[i+1:i+m+1], dominoes[j-m:j] = [l]*m, [r]*m
        return "".join(dominoes)


if __name__ == '__main__':
    sol = Solution()

    t1 = ".L.R...LR..L..",
    print(sol.pushDominoes(*t1))

    t2 = "RR.L",
    print(sol.pushDominoes(*t2))