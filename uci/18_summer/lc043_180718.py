__author__ = 'wangqc'

'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also 
represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def multiply(self, num1, num2):
        ans_len, base = len(num1) + len(num2), ord('0')
        nums1, nums2, ans, pos = self.convert(num1, base), list(self.convert(num2, base)), [0] * ans_len, ans_len - 1
        for i in nums1:
            cur = pos
            for j in nums2:
                ans[cur] += i * j
                ans[cur-1] += ans[cur] // 10
                ans[cur] %= 10
                cur -= 1
            pos -= 1
        return self.revert(ans, base)

    def convert(self, num, base): return map(lambda x: ord(x) - base, num[::-1])

    def revert(self, num, base): return ''.join(map(lambda x: chr(x + base), num)).lstrip('0')

if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.multiply("123", "456")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
