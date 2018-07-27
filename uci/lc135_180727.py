__author__ = 'wangqc'

'''
135. Candy

There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
'''


class Solution:
    # one pass solution
    def candy(self, ratings):
        def aggr(n): return n * (n+1) >> 1
        up = down = prev = count = 0
        for i in range(len(ratings)-1):
            curr = 1 if ratings[i] < ratings[i+1] else -1 if ratings[i] > ratings[i+1] else 0
            if (prev > 0 and not curr) or (prev < 0 and curr >= 0):
                count += aggr(up) + aggr(down) + max(up, down)
                up = down = 0
            if not curr: count += 1
            if curr > 0: up += 1
            if curr < 0: down += 1
            prev = curr
        return count + aggr(up) + aggr(down) + max(up, down) + 1




if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.candy([1, 2, 3, 4, 4, 4, 2, 1, 2, 3])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
