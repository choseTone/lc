__author__ = 'wangqc'

'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(x, self.stack[-1][1]))) if self.stack else self.stack.append((x, x))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]



if __name__ == '__main__':
    from time import time

    t = time()
    minStack = MinStack()
    print('minStack.push(-2)\t --> Return %s' % minStack.push(-2))
    print('minStack.push(0)\t --> Return %s' % minStack.push(0))
    print('minStack.push(-3)\t --> Return %s' % minStack.push(-3))
    print('minStack.getMin()\t --> Return %s' % minStack.getMin())
    print('minStack.pop()\t\t --> Return %s' % minStack.pop())
    print('minStack.top()\t\t --> Return %s' % minStack.top())
    print('minStack.getMin()\t --> Return %s' % minStack.getMin())
    print('time: %.3fms' % (((time() - t)) * 1000))