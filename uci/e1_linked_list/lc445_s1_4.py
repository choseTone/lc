__author__ = 'wangqc'

# https://leetcode.com/problems/add-two-numbers-ii/discuss/250352/Python-Stack-and-Recursion

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbersIter(l1, l2):
    s1, s2 = read(l1), read(l2)
    sum_val, ans = 0, ListNode(0)
    while s1 or s2:
        if s1: sum_val += s1.pop()
        if s2: sum_val += s2.pop()
        sum_val, ans.val = divmod(sum_val, 10)
        head = ListNode(sum_val)
        head.next, ans = ans, head
    return ans if ans.val else ans.next

def read(node):
    s = []
    while node:
        s.append(node.val)
        node = node.next
    return s


def addTwoNumbersRecu(l1, l2):
    len1, len2, carry = getLen(l1), getLen(l2), 0
    if len1 < len2: l1, len1, l2, len2 = l2, len2, l1, len1
    carry = recur(l1, len1, l2, len2)
    if carry:
        head, head.next = ListNode(carry), l1
        return head
    return l1

def recur(l1, len1, l2, len2):
    if not (l1 or l2): return 0
    (len1, l2v, l2n) = (len1-1, 0, l2) if len1 > len2 else (len1, l2.val, l2.next)
    carry, l1v = recur(l1.next, len1, l2n, len2), l1.val
    l1.val = (l1v + l2v + carry) % 10
    return (l1v + l2v + carry) // 10

def getLen(node):
    l = 0
    while node:
        node, l = node.next, l+1
    return l


