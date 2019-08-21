__author__ = 'wangqc'

# https://leetcode.com/problems/super-ugly-number/


import heapq


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        cand = [(p, p, 1) for p in primes]
        nums = [1]
        for _ in range(n - 1):
            nums.append(cand[0][0])
            while cand[0][0] == nums[-1]:
                _, p, i = heapq.heappop(cand)
                heapq.heappush(cand, (nums[i] * p, p, i + 1))
        return nums[n - 1]


if __name__ == '__main__':
    sol = Solution()

    t1 = 212, [2, 7, 13, 19],
    print(sol.nthSuperUglyNumber(*t1))
