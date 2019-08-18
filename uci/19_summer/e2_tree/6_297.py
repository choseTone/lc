__author__ = 'wangqc'
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from utils import TreeNode, Utils


class Codec:

    def serialize(self, root):
        self.str = ""
        def inorder(node):
            if node:
                self.str += f"{node.val} "
                inorder(node.left)
                inorder(node.right)
            else:
                self.str += "# "
        inorder(root)
        return self.str

    def deserialize(self, data):
        def inorder():
            val = next(data)
            if val != "#":
                node = TreeNode(int(val))
                node.left, node.right = inorder(), inorder()
                return node
        data = iter(data.split())
        return inorder()


if __name__ == '__main__':
    codec, util = Codec(), Utils()

    t1 = util.list2tree([1,2,3,None,None,4,5]),
    t2 = codec.deserialize(codec.serialize(*t1))
    print(util.tree2list(t2))