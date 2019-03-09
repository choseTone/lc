__author__ = 'wangqc'

'''
538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the 
original key plus sum of all keys greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        self.sum = 0
        self.convert(root)
        return root

    def convert(self, node):
        if node:
            self.convert(node.right)
            node.val += self.sum
            self.sum = node.val
            self.convert(node.left)


if __name__ == '__main__':
    from time import time

    sol = Solution()

    def list2tree(nums):
        root = TreeNode(int(nums[0]))
        nodeQueue = [root]
        front, index = 0, 1
        while index < len(nums):
            node, item = nodeQueue[front], nums[index]
            front, index = front + 1, index + 1
            if item:
                node.left = TreeNode(item)
                nodeQueue.append(node.left)
            if index >= len(nums):
                break
            item = nums[index]
            index += 1
            if item:
                node.right = TreeNode(item)
                nodeQueue.append(node.right)
        return root

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
    tree = list2tree([5, 2, 13])
    ans = sol.convertBST(tree)
    print('ans: %s\ntime: %.3fms' % (tree2list(ans), ((time() - t)) * 1000))
