__author__ = 'wangqc'

# https://leetcode.com/problems/most-profit-assigning-work/


import bisect


class Solution:
    def maxProfitAssignmentBS(self, difficulty, profit, worker):
        projects = [[0,0]] + sorted([d, p] for d, p in zip(difficulty, profit))
        curr = 0
        for i in range(len(projects)):
            curr = projects[i][1] = max(curr, projects[i][1])
        return sum(projects[bisect.bisect(projects, [w+1,])-1][1] for w in worker)

    def maxProfitAssignment2P(self, difficulty, profit, worker):
        projects = sorted(zip(difficulty, profit))
        i, gain, best, N = 0, 0, 0, len(projects)
        for w in sorted(worker):
            while i < N and w >= projects[i][0]:
                best = max(best, projects[i][1])
                i += 1
            gain += best
        return gain


if __name__ == '__main__':
    sol = Solution()

    t1 = [2,4,6,8,10], [10,20,40,30,50], [4,5,6,7],
    print(sol.maxProfitAssignmentBS(*t1))
    print(sol.maxProfitAssignment2P(*t1))


    t2 = [85,47,57], [24,66,99], [40,25,25],
    print(sol.maxProfitAssignmentBS(*t2))
    print(sol.maxProfitAssignment2P(*t2))