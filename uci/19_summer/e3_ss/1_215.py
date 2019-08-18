__author__ = 'wangqc'
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq, random


class Solution:
    def findKthLargestHeap(self, nums, k):
        nums = [-x for x in nums]
        heapq.heapify(nums)     # O(n)
        for _ in range(k-1):    # +O(klogn)
            heapq.heappop(nums)
        return -nums[0]
    
    def findKthLargestQS(self, nums, k):
        if not nums:
            return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        nums, i, j = left+mid+right, len(left), len(left)+len(mid)
        return self.findKthLargestQS(nums[:i], k) if k <= i else  self.findKthLargestQS(nums[j:], k-j) if k > j else nums[i]


if __name__ == '__main__':
    sol = Solution()

    t1 = [3,2,3,1,2,4,5,5,6], 3
    print(sol.findKthLargestHeap(*t1))
    print(sol.findKthLargestQS(*t1))
