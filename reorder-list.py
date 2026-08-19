'''
    https://leetcode.com/problems/reorder-list/
    143. Reorder List
    You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

from typing import Optional

# Definition for singly-linked list.
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        ll = head
        # find the middle of the LL
        slow, fast = ll, ll.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # self.printList(slow)
        # self.printList(fast)
       
        # break the LL in 2 parts
        second = slow.next
        slow.next = None
        # self.printList(second)
        
        # revese the second part of the LL
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # print('reversed second list')

        # self.printList(prev)

        # merge the LL
        first, second  = ll, prev
        while second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first, second = t1, t2

        # print('merged list')
    

s = Solution()
l=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
s.reorderList(l)
s.printList(l)


