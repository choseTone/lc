__author__ = 'wangqc'

# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1, num2):
        if "0" in (num1, num2):
            return "0"
        M, N, O = len(num1), len(num2), ord("0")

        # 9 x 9 Multiplication Table
        MUL = [[0]*10] + [list(range(10)) for _ in range(9)]
        for i in range(2, 10):
            MUL[i] = [MUL[i-1][j] + MUL[i][j] for j in range(10)]

        def c2i(c):
            return ord(c)-O

        def i2c(i):
            return chr(i+O)

        digits = [0] * (M+N)
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                x, y = c2i(num1[i]), c2i(num2[j])
                xy = digits[i+j+1] + MUL[x][y]
                digits[i+j+1] = xy % 10
                digits[i+j] += xy // 10
        return "".join(map(i2c, digits)).lstrip("0")


if __name__ == '__main__':
    sol = Solution()

    t1 = "20190783", "17282109021"
    print(sol.multiply(*t1))

    t2 = "998", "1921"
    print(sol.multiply(*t2))

    t3 = "0", "8"
    print(sol.multiply(*t3))