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
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        # self.printList(prev)
        return prev

s = Solution()
l = ListNode(1,ListNode(2, ListNode(3, ListNode(4,None))))
# l = ListNode(1,ListNode(2, None))
print(s.printList(s.reverseList([l])))

