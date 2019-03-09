__author__ = 'wangqc'

'''
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''


class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            mark, count, convert = s[0], 0, ''
            for c in s:
                if c == mark:
                    count += 1
                else:
                    convert += str(count) + mark
                    mark, count = c, 1
            s = convert + str(count) + mark
        return s


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.countAndSay(6)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
