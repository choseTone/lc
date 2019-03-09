__author__ = 'wangqc'

'''
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''

import collections


class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for str in strs:
            ans[''.join(sorted(str))].append(str)
        return list(ans.values())


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
