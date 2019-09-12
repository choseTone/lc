__author__ = 'wangqc'

# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/


class Solution:
    def minSwaps(self, data):
        presum = [0]
        for x in data:
            presum.append(presum[-1] + x)
        win = presum[-1]
        return win - max(presum[i+win] - presum[i] for i in range(len(data)-win+1))


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,0,1,0,1],
    print(sol.minSwaps(*t1))

    t2 = [0,0,0,1,0],
    print(sol.minSwaps(*t2))

    t3 = [1,0,1,0,1,0,0,1,1,0,1],
    print(sol.minSwaps(*t3))