__author__ = 'wangqc'

'''
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        topk = []
        for n in nums:
            heapq.heappush(topk, n)
            if len(topk) > k: heapq.heappop(topk)
        return min(topk)


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

