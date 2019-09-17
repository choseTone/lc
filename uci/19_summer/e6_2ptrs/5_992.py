__author__ = 'wangqc'

# https://leetcode.com/problems/subarrays-with-k-different-integers/


from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, A, K):
        def most_k(K):
            counter, i, cnt = Counter(), 0, 0
            for j, a in enumerate(A):
                counter[a] += 1
                while len(counter) > K:
                    counter[A[i]] -= 1
                    if not counter[A[i]]:
                        counter.pop(A[i])
                    i += 1
                cnt += j - i + 1
            return cnt

        return most_k(K) - most_k(K-1)


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2,1,2,3], 2,
    print(sol.subarraysWithKDistinct(*t1))

    t2 = [1,2,1,3,4], 3,
    print(sol.subarraysWithKDistinct(*t2))