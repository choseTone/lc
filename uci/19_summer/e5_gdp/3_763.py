__author__ = 'wangqc'

# https://leetcode.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, S):
        right_idx = {c:i for i, c in enumerate(S)}
        l, r, labels = 0, 0, []
        for i, c in enumerate(S):
            r = max(r, right_idx[c])
            if i == r:
                labels.append(r+1-l)
                l = r+1
        return labels


if __name__ == '__main__':
    sol = Solution()
    t1 = "abcdabefexy",
    print(sol.partitionLabels(*t1))

    t2 = "ababcbacadefegdehijhklij",
    print(sol.partitionLabels(*t2))
