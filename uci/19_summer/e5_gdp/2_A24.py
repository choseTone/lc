__author__ = 'wangqc'

# https://leetcode.com/problems/video-stitching/


class Solution:
    def videoStitching(self, clips, T):
        prev_reach, reach, cnt = -1, 0, 0
        for start, end in sorted(clips):
            if start > reach or reach >= T:
                break
            if start > prev_reach:
                prev_reach = reach
                cnt += 1
            reach = max(reach, end)
        return cnt if reach >= T else -1


if __name__ == '__main__':
    sol = Solution()

    t1 = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10,
    print(sol.videoStitching(*t1))

    t2 = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9,
    print(sol.videoStitching(*t2))

    t3 = [[0,1],[1,2]], 5,
    print(sol.videoStitching(*t3))