import collections, bisect, itertools


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.psum = [{}]
        for x in arr:
            self.psum.append({k: v for k, v in self.psum[-1].items()})
            self.psum[-1][x] = self.psum[-1].get(x, 0) + 1

    def query(self, left: int, right: int, threshold: int) -> int:
        lsum, rsum = self.psum[left], self.psum[right + 1]
        sub = {k: rsum[k] - lsum.get(k, 0) for k in rsum}
        freq, cand = max((v, k) for k, v in sub.items())
        return cand if freq >= threshold else -1

sol = Solution()

t1 = "ababa",
print(sol.maxRepOpt1(*t1))

t1 = "aaabbaaa",
print(sol.maxRepOpt1(*t1))

t1 = "aaaaa",
print(sol.maxRepOpt1(*t1))

t1 = "abcdef",
print(sol.maxRepOpt1(*t1))

