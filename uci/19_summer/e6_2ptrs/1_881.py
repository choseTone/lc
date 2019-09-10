__author__ = 'wangqc'

# https://leetcode.com/problems/boats-to-save-people/


class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        l, r, cnt = 0, len(people)-1, 0
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            cnt += 1
        return cnt + (l == r)


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2], 3,
    print(sol.numRescueBoats(*t1))

    t2 = [3,2,2,1], 3,
    print(sol.numRescueBoats(*t2))

    t3 = [3,5,3,4], 5,
    print(sol.numRescueBoats(*t3))