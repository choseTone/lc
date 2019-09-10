__author__ = 'wangqc'

# https://leetcode.com/problems/diet-plan-performance/


class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        def compare(x):
            return -1 if x < lower else 1 if x > upper else 0
        calories.insert(0, 0)
        score, k_cals = 0, sum(calories[:k])
        for i in range(k, len(calories)):
            k_cals += calories[i] - calories[i-k]
            score += compare(k_cals)
        return score


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2,3,4,5], 1, 3, 3,
    print(sol.dietPlanPerformance(*t1))

    t2 = [3,2], 2, 0, 1,
    print(sol.dietPlanPerformance(*t2))

    t2 = [6,5,0,0], 2, 1, 5,
    print(sol.dietPlanPerformance(*t2))