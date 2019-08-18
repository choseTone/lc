__author__ = 'wangqc'


# https://leetcode.com/problems/digit-count-in-range/


class Solution:
    def digitsCount(self, d, low, high):
        def count(N):
            if not N or (not d and N <= 10):
                return 0
            # cnt is d# caused by lowest digit
            cnt = int(N % 10 > d) + N // 10 - (not d) # last digit is d
            if N // 10:  # last digit is [0,N%10), previous digits contain d
                cnt += str(N // 10).count(str(d)) * (N % 10)
            # count(N//10)*10 is d# caused by previous digits' d# + last digit as [0,9]
            return cnt + count(N // 10) * 10

        return count(high + 1) - count(low)


if __name__ == '__main__':
    sol = Solution()

    t1 = 1, 1, 13
    print(sol.digitsCount(*t1))

    t2 = 3, 100, 250
    print(sol.digitsCount(*t2))
