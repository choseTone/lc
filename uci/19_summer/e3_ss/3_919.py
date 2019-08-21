__author__ = 'wangqc'

# https://leetcode.com/problems/online-election/

from collections import Counter
import bisect


class TopVotedCandidate:
    def __init__(self, persons, times):
        self.counter, self.ts = Counter(), []
        lead, prev = None, 0
        for p, t in zip(persons, times):
            self.counter[p] += 1
            curr = self.counter[p]
            if curr >= prev:
                if lead != p:
                    self.ts.append((t, p))
                    lead = p
                prev = curr


    def q(self, t):
        i = bisect.bisect_left(self.ts, (t+1,)) - 1
        return self.ts[i][1]


if __name__ == '__main__':
    obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(obj.q(3))
    print(obj.q(12))
    print(obj.q(25))
    print(obj.q(15))
    print(obj.q(24))
    print(obj.q(8))
    print(obj.q(17))
