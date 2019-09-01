__author__ = 'wangqc'

# https://leetcode.com/problems/word-search-ii/


class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node["$"] = None

        M, N, hits = len(board), len(board) and len(board[0]), set()

        def dfs(i, j, node, word):
            c, board[i][j] = board[i][j], ""
            if c in node:
                if "$" in node[c]:
                    hits.add(word+c)
                for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0 <= x < M and 0 <= y < N:
                        dfs(x, y, node[c], word+c)
            board[i][j] = c

        for i in range(M):
            for j in range(N):
                dfs(i, j, trie, "")
        return list(hits)


if __name__ == '__main__':
    sol = Solution()

    t1 = [
             ["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]
         ], ["oath","pea","eat","rain"],
    print(sol.findWords(*t1))
