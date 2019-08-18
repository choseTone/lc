__author__ = 'wangqc'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Utils:

    def list2node(self, A):
        head = node = ListNode(0)
        for val in A:
            node.next = ListNode(val)
            node = node.next
        return head.next

    def node2list(self, node):
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans

    def list2tree(self, A):
        root = TreeNode(int(A[0]))
        q = [root]
        front, index = 0, 1
        while index < len(A):
            node, item = q[front], A[index]
            front, index = front + 1, index + 1
            if item is not None:
                node.left = TreeNode(item)
                q.append(node.left)
            if index >= len(A):
                break
            item = A[index]
            index += 1
            if item is not None:
                node.right = TreeNode(item)
                q.append(node.right)
        return root

    def tree2list(self, root):
        queue, out, cur = [root], '', 0
        while cur != len(queue):
            node, cur = queue[cur], cur + 1
            if node:
                out += '%d, ' % node.val
                queue += [node.left, node.right]
            else:
                out += 'null, '
        return out[:-2]
