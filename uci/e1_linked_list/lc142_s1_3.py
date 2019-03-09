__author__ = 'wangqc'

'''
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) 
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it without using extra space? Y
'''

# https://leetcode.com/problems/linked-list-cycle-ii/discuss/249727/Python-Two(Three)-Pointers

'''
Suppose we have such a linked list, with L-long line concatenating with a C-long cycle.
And initially we have two pointers a and b pointing at the head of the linked list. a's stride is 2 and b's stride is 1.
If there is a cycle, a will meet b again in the cycle since a will start to catch up with b
when b enters the cycle (later than a) one step each time (a'stride-b'stride=1).

And suppose a and b meet at point X and the entry of the cycle is E. By saying |EX|=D (in forwarding direction),
b has moved a distance of L+D while a has moved a distance of L+D+KC where K (K>0) is the times that a has been cycling.
Since a's stride is the double of b's, we have L+D+KC = 2L+2D or L+D=KC. So L = C-D +(K-1)C.

Now |XE| is what left for b to reach E (cycle's entry) again. Remember |EX|=D, so |XE|=C-D. Thus, if b moves a distance of L,
which is C-D +(K-1)C, it will be at E. And if we have another pointer c move simultaneously with b but start at the head of linked list,
c will walked through the line whose length is L and also reach the entry point E. So b and c will meet there,
or their meeting point is the entry of the cycle.

To conclude, we can first start moving a(stride 2) and b(stride 1) from the head of linked list. If they meet, there is a cycle.
Then we keep moving b from its meeting point with a, and start moving c from the head of linked list.
When they meet, they meet at the cycle's entry.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def detectCycle(self, head):
        a = b = c = head
        while a and a.next:
            a, b = a.next.next, b.next
            if a == b:
                while b != c:
                    b, c = b.next, c.next
                return b
        return None

'''
Its time complexity is O(n) since the time is bounded with b's walking time(L+D+L < 2n) and space complexity is O(1).
'''