# Definition for singly-linked list.

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


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        t= dummy
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val < l2.val:
                t.next = l1
                l1 = l1.next
            else: 
                t.next = l2
                l2 = l2.next
            t = t.next
        t = l1 or l2

        self.printList(dummy.next)
        self.printList(l1)
        self.printList(l2)
        t.next = list1 or list2
        return dummy.next

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        dummy = ListNode()
        t = dummy

        while l1 and l2:
            if l1.val < l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next

        t.next = l1 or l2
        return dummy.next;

s = Solution()

l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
s.printList((s.mergeTwoLists2(l1, l2)))

