__author__ = 'wangqc'

'''
208. Implement Trie (Prefix Tree)

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations 
are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position 
to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, 
once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using 
the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:
MyCircularQueue circularQueue = new MycircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
 
Note:
All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
'''


class MyCircularQueue:

    def __init__(self, k):
        self.queue, self.size = [0] * k, k
        self.head = self.tail = -1

    def enQueue(self, value):
        if self.isFull(): return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self):
        if self.isEmpty(): return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return True

    def Front(self):
        return -1 if self.head == -1 else self.queue[self.head]

    def Rear(self):
        return -1 if self.tail == -1 else self.queue[self.tail]

    def isEmpty(self):
        return self.head == -1 and self.tail == -1

    def isFull(self):
        return self.head == (self.tail + 1) % self.size


if __name__ == '__main__':

    obj = MyCircularQueue(3)
    print(obj.Front())
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.deQueue())
    print(obj.deQueue())
    print(obj.Front())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Front())
    print(obj.Rear())

