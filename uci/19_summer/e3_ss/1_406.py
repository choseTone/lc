__author__ = 'wangqc'
# https://leetcode.com/problems/queue-reconstruction-by-height/


class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x:(-x[0],x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue


if __name__ == '__main__':
    sol = Solution()

    t1 = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
    print(sol.reconstructQueue(*t1))
