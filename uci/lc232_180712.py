__author__ = 'wangqc'

'''
232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Example:
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty 
operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque 
(double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''


class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.empty():
            self.stack.append(x)
        else:
            cache = self.stack.pop()
            self.push(x)
            self.stack.append(cache)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return not self.stack



if __name__ == '__main__':
    from time import time

    t = time()
    queue = MyQueue()
    print('queue.push(1)\t --> Return %s' % queue.push(1))
    print('queue.push(2)\t --> Return %s' % queue.push(2))
    print('queue.peek()\t --> Return %s' % queue.peek())
    print('queue.pop()\t\t --> Return %s' % queue.pop())
    print('queue.empty()\t --> Return %s' % queue.empty())
    print('queue.push(3)\t --> Return %s' % queue.push(3))
    print('queue.push(4)\t --> Return %s' % queue.push(4))
    print('queue.pop()\t\t --> Return %s' % queue.pop())
    print('queue.peek()\t --> Return %s' % queue.peek())
    print('queue.pop()\t\t --> Return %s' % queue.pop())
    print('queue.pop()\t\t --> Return %s' % queue.pop())
    print('queue.empty()\t --> Return %s' % queue.empty())
    print('time: %.3fms' % (((time() - t)) * 1000))