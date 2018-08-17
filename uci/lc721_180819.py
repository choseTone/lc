__author__ = 'wangqc'

'''
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that 
is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as 
people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely 
have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], 
["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Note:
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
'''

import collections

class Solution:
    def accountsMerge(self, accounts):
        graph = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                graph[email].append(i)
        visited = [False] * len(accounts)

        def dfs(idx, emails):
            if visited[idx]: return
            visited[idx] = True
            for email in accounts[idx][1:]:
                emails.add(email)
                for node in graph[email]:
                    dfs(node, emails)

        ans = []
        for i, account in enumerate(accounts):
            if visited[i]: continue
            name, emails = accounts[i][0], set()
            dfs(i, emails)
            ans.append([name] + sorted(emails))
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    t = time()
    ans = sol.accountsMerge(accounts)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

