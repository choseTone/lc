__author__ = 'wangqc'

'''
65. Valid Number

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before 
implementing one.
'''


class Solution:
    def isNumber(self, s):
        if not s: return False
        s, i = s.strip(), 0
        digit = sign = dot = e = False
        for c in s:
            if not digit and not sign and c in '+-':
                sign = True
            elif c.isdigit():
                digit = sign = True
            elif not dot and c == '.':
                dot = sign = True
            elif digit and not e and c in 'eE':
                e = dot = True
                digit = sign = False
            else: return False
        return digit or False


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.isNumber('2e10')
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
