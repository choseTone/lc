__author__ = 'wangqc'

'''
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        return self.trees(1, n) if n else []

    def node(self, val, left, right):
        node = TreeNode(val)
        node.left, node.right = left, right
        return node

    def trees(self, start, end):
        return [self.node(root, left, right)
                for root in range(start, end+1)
                for left in self.trees(start, root-1)
                for right in self.trees(root+1, end)] or [None]


if __name__ == '__main__':
    from time import time

    sol = Solution()

    def tree2list(head):
        queue, out, cur = [head], '', 0
        while cur != len(queue):
            node, cur = queue[cur], cur + 1
            if node:
                out += '%d, ' % node.val
                queue += [node.left, node.right]
            else: out += 'null, '
        return out[:-2]

    t = time()

    ans = sol.generateTrees(3)
    print('ans: %s\ntime: %.3fms' % (list(map(tree2list, ans)), ((time() - t)) * 1000))
