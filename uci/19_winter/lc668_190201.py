__author__ = 'wangqc'

'''
668. Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from 
the multiplication table?
Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return 
the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9
The 5-th smallest number is 3 (1, 2, 2, 3, 3).

Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]
'''


class Solution:
    def findKthNumber(self, m, n, k):
        lo, hi = 1, m * n
        if k >= hi: return hi
        if m > n: m, n = n, m
        def over(x):
            cnt = 0
            for i in range(1, m + 1):
                c = x // i
                cnt += c if c < n else n
                if cnt >= k: return True    # early break
            return False
        # need to return left end so binary search cannot stop at cnt == k
        # otherwise would return a invalid value(a large prime number) that doesn't belong to the multiplication table
        # e.g. 127(1*127) is out of the 42*34 multipication table and binary research would return 127 if it stops at cnt == k
        # since there is no 127 in the table so (cnt <= 126) == (cnt <= 127)
        while lo < hi:
            mid = lo + hi >> 1
            if over(mid): hi = mid
            else: lo = mid + 1
        return lo


if __name__ == '__main__':
    sol = Solution()
    argv = 42, 34, 401
    ans = sol.findKthNumber(*argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

