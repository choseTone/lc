__author__ = 'wangqc'
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        ans = []
        for i in sorted(intervals):
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1], i[1])
        return ans


if __name__ == '__main__':

    sol = Solution()

    t1 = [[1,3],[2,6],[8,10],[15,18]],
    print(sol.merge(*t1))

    t2 = [[1,4],[4,5]],
    print(sol.merge(*t2))

