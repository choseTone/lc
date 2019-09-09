__author__ = 'wangqc'

# https://leetcode.com/problems/odd-even-jump/


class Solution:
    def oddEvenJumps(self, A):
        N = len(A)

        def next_steps(idx):
            steps, stack = [0] * N, []
            for i in idx:
                while stack and i > stack[-1]:
                    steps[stack.pop()] = i
                stack.append(i)
            return steps

        odd_next = next_steps(sorted(range(N), key=lambda i: A[i]))
        even_next = next_steps(sorted(range(N), key=lambda i: -A[i]))
        odds, evens = [False]*(N-1)+[True], [False]*(N-1)+[True]
        for i in range(N-2, -1, -1):
            if odd_next[i]:
                odds[i] = evens[odd_next[i]]
            if even_next[i]:
                evens[i] = odds[even_next[i]]
        return sum(odds)


if __name__ == '__main__':
    sol = Solution()

    t1 = [10,13,12,14,15],
    print(sol.oddEvenJumps(*t1))

    t2 = [2,3,1,1,4],
    print(sol.oddEvenJumps(*t2))

    t3 = [6,6,6,6,6,6],
    print(sol.oddEvenJumps(*t3))