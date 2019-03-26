__author__ = 'wangqc'

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/255418/Python-Recursive-Preorder

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        self.data = ''

        def dfs(node):
            if node:
                self.data += '%s ' % node.val
                dfs(node.left), dfs(node.right)
            else:
                self.data += '# '

        dfs(root)
        return self.data

    def deserialize(self, data):
        def dfs():
            val = next(data)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left, node.right = dfs(), dfs()
            return node

        data = iter(data.split())
        return dfs()