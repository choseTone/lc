__author__ = 'wangqc'

# https://leetcode.com/problems/best-meeting-point/


class Solution:
    def canJump(self, nums):
        reach = 0
        for i, x in enumerate(nums):
            if reach < i:
                return False
            reach = max(reach, i+x)
        return True



if __name__ == '__main__':
    sol = Solution()

    t1 = [2,3,1,1,4],
    print(sol.canJump(*t1))

    t2 = [3,2,1,0,4],
    print(sol.canJump(*t2))