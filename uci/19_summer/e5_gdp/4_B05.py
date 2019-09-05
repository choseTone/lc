__author__ = 'wangqc'

# https://leetcode.com/problems/filling-bookcase-shelves/


class Solution:
    def minHeightShelves(self, books, shelf_width):
        dp = [0]
        for i in range(len(books)):
            j, w = i, shelf_width
            while j >= 0 and w - books[j][0] >= 0:
                w -= books[j][0]
                j -= 1
            dp.append(min(dp[k]+max(books[x][1] for x in range(k,i+1)) for k in range(j+1,i+1)))
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4,
    print(sol.minHeightShelves(*t1))

    t2 = [[1,3],[2,4],[3,2]], 6,
    print(sol.minHeightShelves(*t2))