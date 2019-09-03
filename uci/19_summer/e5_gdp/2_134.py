__author__ = 'wangqc'

# https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        N, start, remain = len(gas), 0, 0
        for i, curr in enumerate([g-c for g,c in zip(gas, cost)]):
            if curr + remain < 0:
                start, remain = i + 1, 0
            else:
                remain += curr
        return start


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2,3,4,5], [3,4,5,1,2],
    print(sol.canCompleteCircuit(*t1))

    t2 = [2,3,4], [3,4,3],
    print(sol.canCompleteCircuit(*t2))