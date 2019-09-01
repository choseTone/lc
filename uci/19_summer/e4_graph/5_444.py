__author__ = 'wangqc'

# https://leetcode.com/problems/sequence-reconstruction/

from collections import defaultdict


class Solution:
    def sequenceReconstruction(self, org, seqs):
        dst, src, nodes = defaultdict(set), defaultdict(set), set()
        for seq in seqs:
            nodes |= set(seq)
            for i, node in enumerate(seq[1:]):
                src[node].add(seq[i])
                dst[seq[i]].add(node)
        if len(nodes) != len(org):
            return False
        q, path = [node for node in range(1, len(org)+1) if not src[node]], []
        while len(q) == 1:
            node = q.pop()
            path.append(node)
            for nei in dst[node]:
                src[nei].remove(node)
                if not src[nei]:
                    q.append(nei)
        return path == org


if __name__ == '__main__':
    sol = Solution()

    t1 = [1,2,3], [[1,2],[1,3]],
    print(sol.sequenceReconstruction(*t1))

    t2 = [4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]],
    print(sol.sequenceReconstruction(*t2))
