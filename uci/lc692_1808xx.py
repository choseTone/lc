__author__ = 'wangqc'

'''
692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word 
with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''

import heapq, collections

class Node:
    def __init__(self, freq, word):
        self.freq, self.word = freq, word

    def __gt__(self, other):
        return self.word < other.word if self.freq == other.freq else self.freq > other.freq

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word

class Solution:
    def topKFrequent(self, words, k):
        freqs, top = collections.Counter(words), []
        for word, freq in freqs.items():
            heapq.heappush(top, Node(freq, word))
            if len(top) > k:
                heapq.heappop(top)
        return [heapq.heappop(top).word for _ in range(k)][::-1]


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

