__author__ = 'wangqc'


# https://leetcode.com/problems/sliding-window-median/

import heapq


class Solution:
    def medianSlidingWindow(self, nums, k):
        small, large = [(-x, i) for i, x in enumerate(nums[:k])], []
        heapq.heapify(small)

        def heap_move(h1, h2):
            x, i = heapq.heappop(h1)
            heapq.heappush(h2, (-x,i))

        def get_median():
            return float(large[0][0]) if k&1 else (large[0][0]-small[0][0])/2.

        def lazy_del(h, i):
            while h and h[0][1] <= i:
                heapq.heappop(h)

        for _ in range(k+1>>1):
            heap_move(small, large)
        medians = [get_median()]
        for i, x in enumerate(nums[k:]):
            if x > large[0][0]:
                heapq.heappush(large, (x, i+k))
                if nums[i] < large[0][0]:
                    heap_move(large, small)
            else:
                heapq.heappush(small, (-x, i+k))
                if nums[i] >= large[0][0]:
                    heap_move(small, large)
            lazy_del(small, i)
            lazy_del(large, i)
            medians.append(get_median())
        return medians


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,3,-1,-3,5,3,6,7], 3,
    print(sol.medianSlidingWindow(*t1))

    t2 = [1,4,2,3], 4,
    print(sol.medianSlidingWindow(*t2))
