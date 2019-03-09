__author__ = 'wangqc'

'''
433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE 
single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a 
valid gene string.
Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate 
from "start" to "end". If there is no such a mutation, return -1.

Note:
Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 

Example 1:
start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]
return: 1
 
Example 2:
start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
return: 2
 
Example 3:
start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
return: 3
'''

class Solution(object):
    def minMutation(self, start, end, bank):
        record = {s: 1 for s in bank + [start]}
        if end in record:
            queue = [(start, 0)]
            while queue:
                curr, step = queue.pop(0)
                if curr == end: return step
                record[curr] -= 1
                for s in bank:
                    if record[s] and self.valid(curr, s):
                        queue.append((s, step + 1))
        return -1

    def valid(self, a, b):
        mute = False
        for i, c in enumerate(a):
            if c != b[i]:
                if mute: return False
                else: mute = True
        return mute


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

