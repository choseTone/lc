__author__ = 'wangqc'
# https://leetcode.com/problems/palindrome-linked-list/

import collections, heapq


class Solution:
    def rearrangeBarcodes(self, barcodes):
        pq = [(-v,k) for k,v in collections.Counter(barcodes).items()]
        heapq.heapify(pq)
        ret = []
        prev = prev_cnt = 0
        while pq:
            # add most frequent code to ret each time,
            # but code i can't be identical with the code i-1
            # so use prev, curr trick to avoid that case
            curr_cnt, curr = heapq.heappop(pq)
            ret.append(curr)
            if prev_cnt:
                heapq.heappush(pq, (prev_cnt, prev))
            prev, prev_cnt = curr, curr_cnt+1
        return ret


if __name__ == '__main__':

    sol = Solution()

    t1 = [1,1,1,2,2,2],
    print(sol.rearrangeBarcodes(*t1))

    t2 = [1,1,1,1,2,2,3,3],
    print(sol.rearrangeBarcodes(*t2))
