__author__ = 'wangqc'

from utils import Utils

class Solution:
    def inorder_traversal(self, root):
        nodes = []
        while root:
            if root.left:
                pred = root.left
                while pred.right and pred.right != root:
                    pred = pred.right
                if pred.right:
                    nodes.append(root.val)
                    root = root.right
                    pred.right = None
                else:
                    pred.right = root
                    root = root.left
            else:
                nodes.append(root.val)
                root = root.right
        return nodes

    def count_nodes(self, root, N=0):
        cnt, left = 0, None
        while root:
            if root.left:
                pred = root.left
                while pred.right and pred.right != root:
                    pred = pred.right
                if pred.right:
                    cnt += 1
                    if not N & 1 and cnt == N >> 1:
                        left = root.val
                    if N and cnt-1 == N >> 1:
                        return root.val if N & 1 else (left + root.val) / 2
                    root = root.right
                    pred.right = None
                else:
                    pred.right = root
                    root = root.left
            else:
                cnt += 1
                if not N & 1 and cnt == N >> 1:
                    left = root.val
                if N and cnt-1 == N >> 1:
                    return root.val if N & 1 else (left + root.val) / 2
                root = root.right
        return cnt

    def find_median(self, root):
        return self.count_nodes(root, self.count_nodes(root))


if __name__ == '__main__':
    sol, util = Solution(), Utils()

    t1 = util.list2tree([20, 8, 22, 4, 12, None, None, None, None, 10, 14]),
    print(sol.inorder_traversal(*t1))
    print(sol.find_median(*t1))

    t2 = util.list2tree([20, 8, 22, 4, 12, None, None, None, 6, 10, 14]),
    print(sol.inorder_traversal(*t2))
    print(sol.find_median(*t2))

