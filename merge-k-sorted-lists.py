
'''
    23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
https://leetcode.com/problems/merge-k-sorted-lists/description/
'''

'''
    Solutions:
    create a loop for each lists of items in the list, merge two lists first and keep doing it unill all the lists softed
'''


from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKListsFunction(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0 :
            return None


        while len(lists) > 1:
            mergedKList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedKList.append(self.mergeListFunction(l1, l2))

            lists = mergedKList

        return lists[0]

    def mergeListFunction(self, l1, l2):
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        temp.next = l1 or l2

        return dummy.next

    def printList(self, ll: Optional[ListNode]):
        print('---------')
        while ll:
            print(ll.val)
            ll = ll.next

s = Solution()
# [[1,4,5],[1,3,4],[2,6]]
l1 = ListNode(1, ListNode(4, ListNode(5, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
l3 = ListNode(2, ListNode(6, None))

s.printList(s.mergeKListsFunction([l1, l2, l3]))





