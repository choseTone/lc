__author__ = 'wangqc'

'''
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array 
contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution:
    def plusOne(self, digits):
        i, carry = len(digits) - 1, True
        while i >= 0 and carry:
            digits[i] = (digits[i] + 1) % 10
            carry, i = not digits[i], i-1
        return [1] + digits if carry else digits


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.plusOne([9,9,9])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))