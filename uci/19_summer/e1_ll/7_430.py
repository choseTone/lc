__author__ = 'wangqc'


# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        if not head:
            return None
        dummy, stack = Node(0, None, head, None), [head]
        prev = dummy
        while stack:
            node = stack.pop()
            node.prev, prev.next = prev, node
            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
            prev = node
        dummy.next.prev = None
        return dummy.next


if __name__ == '__main__':
    pass
    # data structure for this problem too fan le
