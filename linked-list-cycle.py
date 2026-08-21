
from typing import Optional
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hl = head
        slow, fast = hl, hl
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return true

        return False

l = ListNode(1,ListNode(2, ListNode(3, ListNode(4,None))))
s = Solution()
print( s.hasCycle(l))
