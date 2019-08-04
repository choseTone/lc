import collections

class Solution:
    def unique_number(self, A):
        one = two = A[0]
        found = False
        for x in A[1:]:
            if x != one:
                if not found:
                    found = True
                    two = x
                else:
                    return one
            elif found:
                break
        return two



sol = Solution()
print(sol.unique_number([2,1,1,1,1]))
print(sol.unique_number([1,2,1,1,1]))
print(sol.unique_number([1,1,2,1,1]))
print(sol.unique_number([1,1,1,2,1]))
print(sol.unique_number([1,1,1,1,2]))


