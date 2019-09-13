__author__ = 'wangqc'

# https://leetcode.com/problems/3sum-with-multiplicity/

from collections import Counter


class Solution:
    def threeSumMulti(self, A, target):
        counter, cnt, M = Counter(A), 0, 10**9 + 7
        keys, N = sorted(counter), len(counter)
        for i, x in enumerate(keys):
            T, j, k = target-x, i, N-1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:
                    if i < j < k:
                        cnt += counter[x]*counter[y]*counter[z]
                    elif i == j == k:
                        cnt += counter[x]*(counter[x]-1)*(counter[x]-2) // 6
                    else:
                        cnt += (counter[y])*(counter[y]-1)//2 * counter[[x,z][i==j]]
                    cnt %= M

                    j, k = j+1, k-1
        return cnt


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,1,2,2,3,3,4,4,5,5], 8,
    print(sol.threeSumMulti(*t1))

    t2 = [1,1,2,2,2,2], 5,
    print(sol.threeSumMulti(*t2))