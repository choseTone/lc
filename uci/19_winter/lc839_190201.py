__author__ = 'wangqc'

'''
839. Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.
For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but 
"star" is not similar to "tars", "rats", or "arts".
Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and 
"arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group 
if and only if it is similar to at least one other word in the group.
We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

Example 1:

Input: ["tars","rats","arts","star"]
Output: 2
Note:

A.length <= 2000
A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
'''

import collections, itertools

class Solution:
    def numSimilarGroups(self, A):
        n, m = len(A), len(A[0])
        p, sz = list(range(n)), [1] * n
        def find(x):
            if p[x] != x: p[x] = find(p[x])
            return p[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if sz[px] > sz[py]: px, py = py, px
                p[px], sz[py] = py, sz[py] + sz[px]
        # number of component groups, use union find
        # approach 1: check all similar words of each word, o(n*m^2)
        # approach 2: check all the pairs in word list, o(n^2)
        if n > m * m:   # small word use approach 1
            pool = collections.defaultdict(set)
            for i, w in enumerate(A):
                for x, y in itertools.combinations(range(m), 2):
                    pool[w[:x]+w[y]+w[x+1:y]+w[x]+w[y+1:]].add(i)   # swap w[x], w[y]
            for i1, w in enumerate(A):
                for i2 in pool[w]: union(i1, i2)
        else:           # large word use approach 2
            for (i1, w1), (i2, w2) in itertools.combinations(enumerate(A), 2):
                if sum(c1 != c2 for c1, c2 in zip(w1, w2)) <= 2: union(i1, i2)
        return sum(p[x] == x for x in range(n))


if __name__ == '__main__':
    sol = Solution()
    argv = ["tars","rats","arts","star"]
    ans = sol.numSimilarGroups(argv)
    print('Input : %s\nOutput: %s' % (argv, ans))

