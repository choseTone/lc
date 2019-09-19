__author__ = 'wangqc'

# https://leetcode.com/problems/basic-calculator/


class Solution:
    def calculate(self, s):
        ans, i, N, O, sign = 0, 0, len(s), ord("0"), [1, 1]
        while i < N:
            if s[i].isdigit():
                x = 0
                while i < N and s[i].isdigit():
                    x = x * 10 + ord(s[i]) - O
                    i += 1
                ans += x * sign.pop()
            else:
                if s[i] == ")":
                    sign.pop()
                if s[i] in "(+-":
                    sign.append(sign[-1] * (-1 if s[i] == "-" else 1))
                i += 1
        return ans


if __name__ == '__main__':
    sol = Solution()

    t1 = "1 + 1",
    print(sol.calculate(*t1))

    t2 = "1 - (2-(3+4))",
    print(sol.calculate(*t2))

    t3 = "(1+(4+5+2)-3)+(6+8)",
    print(sol.calculate(*t3))