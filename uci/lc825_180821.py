__author__ = 'wangqc'

'''
825. Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 
Person A will NOT friend request person B (B != A) if any of the following conditions are true:
age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.
Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.
How many total friend requests are made?

Example 1:
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:
Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Notes:
1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
'''


class Solution:
    def numFriendRequests(self, ages):
        ages_num, ages_sum = [0] * 121, [0] * 121
        for age in ages:
            ages_num[age] += 1
        for i in range(1, 121):
            ages_sum[i] = ages_sum[i-1] + ages_num[i]
        return sum((ages_sum[i] - ages_sum[i//2+7] - 1) * ages_num[i] for i in range(15, 121) if ages_num[i])


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.numFriendRequests([20,30,100,110,120])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

