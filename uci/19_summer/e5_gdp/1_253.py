__author__ = 'wangqc'

# https://leetcode.com/problems/non-overlapping-intervals/


class Solution:
    def minMeetingRooms(self, intervals):
        starts, ends = sorted(s for s,_ in intervals), sorted(e for _,e in intervals)
        cnt = i = 0
        for start in starts:
            if start < ends[i]:
                cnt += 1
            else:
                i += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [[0, 30],[5, 10],[15, 20]],
    print(sol.minMeetingRooms(*t1))

    t2 = [[7,10],[2,4]],
    print(sol.minMeetingRooms(*t2))