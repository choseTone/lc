__author__ = 'wangqc'
# https://leetcode.com/problems/palindrome-linked-list/

from utils import ListNode, Utils


class Solution:
    def isPalindrome(self, head):
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, rev, slow = rev, slow, slow.next
        if fast:  # pass the mid point of an odd-length list
            slow = slow.next
        while slow and slow.val == rev.val:
            slow, rev = slow.next, rev.next
        return not rev


if __name__ == '__main__':

    sol, util = Solution(), Utils()

    t1 = util.list2node([1,2]),
    print(sol.isPalindrome(*t1))

    t2 = util.list2node([1,2,2,1]),
    print(sol.isPalindrome(*t2))
