__author__ = 'wangqc'

# https://leetcode.com/problems/stamping-the-sequence/


class Solution:
    def movesToStamp(self, stamp, target):
        M, N, dead = len(stamp), len(target), set()

        def dp(i, j, idx):
            if j == N:
                return idx if i == M else []
            elif (i, j) not in dead:
                if i == M:
                    for ni in range(M):
                        candidate = dp(ni, j, [j-ni]+idx)
                        if candidate:
                            return candidate
                elif stamp[i] == target[j]:
                    candidate = dp(i+1, j+1, idx)
                    return candidate if candidate else dp(0, j+1, idx+[j+1])
                dead.add((i, j))
            return []

        return dp(0, 0, [0])


if __name__ == '__main__':
    sol = Solution()

    t1 = "qxq", "qxqxqxqqxqxqqxqxqxqqxqxqqqxqqxqqqxqqxxqxqqxqqqxqqq"
    print(sol.movesToStamp(*t1))

    t2 = "abca", "aabcaca"
    print(sol.movesToStamp(*t2))

    t3 = "abacd", "ababacd"
    print(sol.movesToStamp(*t3))