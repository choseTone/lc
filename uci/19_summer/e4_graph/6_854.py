__author__ = 'wangqc'

# https://leetcode.com/problems/k-similar-strings/


class Solution:
    def kSimilarity(self, A, B):
        N = len(B)

        def nei(X):
            i = 0
            while X[i] == B[i]:
                i += 1
            return [X[:i]+X[j]+X[i+1:j]+X[i]+X[j+1:] for j in range(i+1, N) if X[j] == B[i]]

        q, seen, = [(A, 0)], {A}
        for X, d in q:
            if X == B:
                return d
            for Y in nei(X):
                if Y not in seen:
                    seen.add(Y)
                    q.append((Y, d+1))


if __name__ == '__main__':
    sol = Solution()

    t1 = "ab", "ba",
    print(sol.kSimilarity(*t1))

    t2 = "aabc", "abca",
    print(sol.kSimilarity(*t2))