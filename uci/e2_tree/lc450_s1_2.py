__author__ = 'wangqc'

'''
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
'''

'''
For a BST tree, a node.val is larger than any node values from left branch and smaller than any node values from right branch.

Now let's think about the inital next, it returns the most left node in the tree, then the next node is its parent node. 
Then the next node is the most left node in parent node's right branch if there is one, otherwise it's the grandparent node.

So here is a pattern that we return a parent node in the reverse order (child->parent->grandparent) and 
a LIFO stack could be implemented here.

Step1. We keep pushing left node into the stack until reach a leaf. Then there is no smaller value. 
I abstracted this step as a function pushLeft.
Step2. We pop the last node in the stack, which is the smallest node, as the next node. Let's mark it as X.
Step3. Now we need to consider right branch. If there is a right branch, all nodes there have a larger value than X, 
but smaller value than X's parent node since X is a left node. Thus, the next node after X should be the most left node in the right branch. 
And we could repeat Step1 passing node.right as a root node. If there is no right branch, we just repeat Step2.

Stack will be updated in such way that any new added nodes a have larger value than current last node(X's parent) and later node 
has smaller value(left node value < parent value). So the last node in the stack will keep being the smallest 
which could be safely popped out and return for next.

Initially we pushLeft the root node. If there is no left branch in root node, only root node would be pushed.

When stack is empty, there is no node left in the iterator and hasNext returns false.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.push(root)

    def next(self):
        if self.hasNext():
            node = self.stack.pop()
            if node.right: self.push(node.right)
            return node.val

    def hasNext(self):
        return bool(self.stack)

    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left

'''
The max length of the stack won't exceed tree's height. So space complexity is O(h). 
And average next time complexity is O(1)(O(2)) since all nodes will be only pushed and popped once.
'''