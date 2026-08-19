'''
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, ll: Optional[ListNode]):
        print('---------')
        while ll:
            print(ll.val)
            ll = ll.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right= right.next

        left.next = left.next.next

        return dummy.next
s = Solution()
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
x = s.removeNthFromEnd(l,2)
s.printList(x)

