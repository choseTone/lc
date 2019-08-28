__author__ = 'wangqc'

# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, A, B, S):
        p = list(range(26))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = sorted([find(x), find(y)])
            if px != py:
                p[py] = px

        for a, b in zip(A, B):
            union(ord(a)-97, ord(b)-97)
        return "".join(chr(find(ord(c)-97)+97) for c in S)


if __name__ == '__main__':
    sol = Solution()

    t1 = "leetcode", "programs", "sourcecode"
    print(sol.smallestEquivalentString(*t1))

    t2 = "parker", "morris", "parser"
    print(sol.smallestEquivalentString(*t2))