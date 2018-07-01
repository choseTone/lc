__author__ = 'wangqc'

'''
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
import heapq


class Solution:
    def topKFrequent_sort(self, nums, k):
        counter, n, ans = {}, len(nums), []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        return sorted(counter.keys(), key=lambda x: counter[x], reverse=True)[:k]

    def topKFrequent_bucket(self, nums, k):
        counter, n, ans = {}, len(nums), []
        bucket = [[] for _ in range(n+1)]
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for num, freq in counter.items():
            bucket[freq].append(num)
        # choose top k freq' numbers from bucket, need to remove extra equal-freq numbers
        while len(bucket[n]) < k - len(ans):
            ans += bucket[n]
            n -= 1
        return ans + bucket[n][:k - len(ans)]

    def topKFrequent_heap(self, nums, k):
        counter, n, ans = {}, len(nums), []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        # pop the number with smallest freq out of the full-filled heap
        for num, freq in counter.items():
            heapq.heappush(ans, (freq, num))
            if len(ans) > k:
                heapq.heappop(ans)
        return [i[1] for i in ans]


if __name__ == '__main__':
    from time import time
    from random import randint

    sol = Solution()
    nums, k = [randint(1, 100) for _ in range(2**15)], 100
    # nums, k = list(range(1, 2**15)), 2**14
    t1 = time()
    ans1 = sol.topKFrequent_sort(nums, k)
    t2 = time()
    ans2 = sol.topKFrequent_bucket(nums, k)
    t3 = time()
    ans3 = sol.topKFrequent_heap(nums, k)
    t4 = time()
    # sol1 time: 4.80ms; sol1 time: 15.97ms; sol1 time: 4.54ms
    print('sol1 ans: %s\ntime: %.3fms' % (ans1, ((t2 - t1)) * 1000))
    print('sol2 ans: %s\ntime: %.3fms' % (ans2, ((t3 - t2)) * 1000))
    print('sol3 ans: %s\ntime: %.3fms' % (ans3, ((t4 - t3)) * 1000))
