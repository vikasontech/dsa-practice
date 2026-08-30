'''
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

https://leetcode.com/problems/reverse-linked-list/description/
'''
'''
'''

from typing import Optional

# Definition for singly-linked list.
#
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print('radhe radhe')
        prev, current = None, head[0]

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # self.printList(prev)
        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head[0]
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
s = Solution()
l = ListNode(1,ListNode(2, ListNode(3, ListNode(4,None))))
# l = ListNode(1,ListNode(2, None))
s.printList(s.reverseList2([l]))

