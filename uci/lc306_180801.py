__author__ = 'wangqc'

'''
306. Additive Number

Additive number is a string whose digits can form additive sequence.
A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent 
number in the sequence must be the sum of the preceding two.
Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?
'''


class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]
                if i > 1 and a[0] == '0' or j > i+1 and b[0] == '0':
                    continue
                while j < n:
                    c = str(int(a) + int(b))
                    if not num[j:].startswith(c):
                        break
                    if num[j:] == c:
                        return True
                    j += len(c)
                    a, b = b, c
        return False



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.isAdditiveNumber("199100199")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
