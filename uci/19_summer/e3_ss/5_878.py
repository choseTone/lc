__author__ = 'wangqc'


# https://leetcode.com/problems/nth-magical-number/


class Solution:
    def nthMagicalNumberMath(self, N, A, B):
        def gcd(a, b):
            return gcd(b, a%b) if a%b else b

        L = A * B // gcd(A, B)
        M = L // A + L // B - 1
        x, r = divmod(N, M)
        q = [0, 0]
        for _ in range(r+1):
            if q[0] <= q[1]:
                q[0] += A
            else:
                q[1] += B
        return (x * L + min(q)) % (10 ** 9 + 7)

    def nthMagicalNumberBS(self, N, A, B):
        def gcd(a, b):
            return gcd(b, a%b) if a%b else b

        lo, hi, L = 2, N * min(A, B), A * B // gcd(A, B)
        while lo < hi:
            mid = lo + hi >> 1
            if mid // A + mid // B - mid // L < N:
                lo = mid + 1
            else:
                hi = mid
        return lo % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()

    t1 = 5, 2, 4,
    print(sol.nthMagicalNumberMath(*t1))
    print(sol.nthMagicalNumberBS(*t1))

    t2 = 8, 3, 21,
    print(sol.nthMagicalNumberMath(*t2))
    print(sol.nthMagicalNumberBS(*t2))
