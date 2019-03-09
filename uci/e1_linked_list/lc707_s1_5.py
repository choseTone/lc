__author__ = 'wangqc'

'''
707. Design Linked List

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. 
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.

addAtHead(val) : Add a node of value val before the first element of the linked list. 
After the insertion, the new node will be the first node of the linked list.

addAtTail(val) : Append a node of value val to the last element of the linked list.

addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. 
If index equals to the length of linked list, the node will be appended to the end of linked list. 
If index is greater than the length, the node will not be inserted.

deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Note:
All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
'''

# https://leetcode.com/problems/design-linked-list/discuss/251789/Python-Clean-Two-Ends-Iteration

'''
Add multiple helper functions to make code cleaner.
One improvement is to iterate from one of two ends instead of just the head in get, addAtIndex and deleteAtIndex.
We start iteration from the head If index is in the first half of the linked list (0, self.sz/2),
while we start iteration from the tail if index is in the second half (self.sz/2, self.sz).
In such way, iteration time could be halved.
'''

class Node:

    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class MyLinkedList:

    def __init__(self):
        self.h = self.t = Node(-1)
        self.h.next, self.t.prev = self.h, self.t
        self.sz = 0

    def add(self, refer, node):
        node.prev, node.next = refer.prev, refer
        refer.prev = node.prev.next = node
        self.sz += 1

    def rm(self, node):
        node.next.prev, node.prev.next = node.prev, node.next
        self.sz -= 1

    def fwd(self, i, j, node):
        for _ in range(i, j): node = node.next
        return node

    def bck(self, j, i, node):
        for _ in range(i, j): node = node.prev
        return node

    def getNode(self, i):
        if 0 <= i < self.sz >> 1:
            return self.fwd(0, i, self.h.next)
        elif self.sz >> 1 <= i < self.sz:
            return self.bck(self.sz - 1, i, self.t.prev)

    def get(self, i):
        return self.getNode(i).val if 0 <= i < self.sz else -1

    def addAtHead(self, val):
        self.add(self.h.next, Node(val))

    def addAtTail(self, val):
        self.add(self.t, Node(val))

    def addAtIndex(self, i, val):
        if 0 <= i < self.sz:
            self.add(self.getNode(i), Node(val))
        elif i == self.sz:
            self.addAtTail(val)

    def deleteAtIndex(self, i):
        if 0 <= i < self.sz: self.rm(self.getNode(i))

'''
One thing should be noticed is that we need to decide the way to add a node. We can either add it before or after a refer node. 
In either way, we should implement addAtHead, addAtTail and addAtIndex accordingly. For me, I choose to add a node 
before a refer node so addAtIndex implementation could be a bit cleaner. In this case, the refer node is getNode(i) 
(We add the node before the ith node so that it becomes the new ith node.) Then in addAtHead, the refer node should be self.head.next.
And another tricky issue is that addAtIndex(self.sz) is possible which equals to addAtTail. We could just redirect to it. 
In such way, we don't need to worry about cases like addAtIndex(0) when list is empty.
'''