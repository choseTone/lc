__author__ = 'wangqc'

# https://leetcode.com/problems/shopping-offers/


class Solution:
    def shoppingOffers(self, price, special, needs):
        memo, N = {}, len(needs)

        def dp(needs):
            if needs not in memo:
                cost = sum(n*p for n,p in zip(needs, price))
                for s in special:
                    undo = tuple(n-s[i] for i, n in enumerate(needs) if n >= s[i])
                    if len(undo) == N:
                        cost = min(cost, dp(undo) + s[N])
                memo[needs] = cost
            return memo[needs]

        return dp(tuple(needs))


if __name__ == '__main__':
    sol = Solution()

    t1 = [2,5], [[3,0,5],[1,2,10]], [3,2],
    print(sol.shoppingOffers(*t1))

    t2 = [2,3,4],[[1,1,0,4],[2,2,1,9]],[1,2,1],
    print(sol.shoppingOffers(*t2))