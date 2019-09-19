__author__ = 'wangqc'

# https://leetcode.com/problems/basic-calculator-iii/


class Solution:
    def calculate(self, s):
        i, ops, vals, N, O = 0, [], [], len(s), ord("0")
        while i < N:
            if s[i].isdigit():
                x = 0
                while i < N and s[i].isdigit():
                    x = x * 10 + ord(s[i]) - O
                    i += 1
                vals.append(x)
            else:
                c = s[i]
                if c == "(":
                    ops.append(c)
                if c == ")":
                    while ops[-1] != "(":
                        vals.append(self.operate(ops.pop(), vals.pop(), vals.pop()))
                    ops.pop()
                if c in "+-*/":
                    while ops and ops[-1] != "(" and not(ops[-1] in "+-" and c in "*/"):
                        vals.append(self.operate(ops.pop(), vals.pop(), vals.pop()))
                    ops.append(c)
                    if c == "-":
                        j = i-1
                        while j >= 0 and s[j] == " ":
                            j -= 1
                        if s[j] == "(" or not vals:
                            vals.append(0)
                i += 1
        while ops:
            vals.append(self.operate(ops.pop(), vals.pop(), vals.pop()))
        return min(max(-2**31, vals.pop()), 2**31-1)

    def operate(self, op, y, x):
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x // y
        return 0


if __name__ == '__main__':
    sol = Solution()

    t1 = "-1+4*3/3/3",
    print(sol.calculate(*t1))

    t2 = "2*(5+5*2)/3+(6/2+8)",
    print(sol.calculate(*t2))

    t3 = "(2+6* 3+5- (3*14/7+2)*5)+3",
    print(sol.calculate(*t3))

    t4 = "1 - (-7)",
    print(sol.calculate(*t4))