__author__ = 'wangqc'

'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

from functools import reduce

class Solution:
    def letterCombinations(self, digits):
        dials = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return reduce(lambda acc, digit: [x + y for x in acc for y in dials[digit]], digits, [''])

if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.letterCombinations("23")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
