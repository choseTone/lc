__author__ = 'wangqc'

# https://leetcode.com/problems/find-peak-element/


from collections import Counter

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        counter = Counter(nums)
        tri = [[0,0,0]] if counter[0] > 2 else []
        pos, neg = [x for x in counter if x >= 0], [x for x in counter if x < 0]
        for n in neg:
            for p in pos:
                x = -p-n
                if x in counter:
                    if x in {p, n} and counter[x] > 1:
                        tri.append([n,x,p])
                    if x < n:
                        tri.append([x,n,p])
                    if x > p:
                        tri.append([n,p,x])
        return tri


if __name__ == '__main__':
    sol = Solution()

    t1 = [-1, 0, 1, 2, -1, -4],
    print(sol.threeSum(*t1))
