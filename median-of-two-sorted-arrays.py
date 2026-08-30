'''
    https://leetcode.com/problems/median-of-two-sorted-arrays/description/
'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        # Always binary-search the smaller array
        if len(a) > len(b):
            a, b = b, a

        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a)

        while True:
            i = (l + r) // 2
            j = half - i

            aLeft = a[i - 1] if i > 0 else float("-inf")
            aRight = a[i] if i < len(a) else float("inf")

            bLeft = b[j - 1] if j > 0 else float("-inf")
            bRight = b[j] if j < len(b) else float("inf")

            print("i:", i, "j:", j)
            print("aLeft:", aLeft)
            print("aRight:", aRight)
            print("bLeft:", bLeft)
            print("bRight:", bRight)

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2

            elif aLeft > bRight:
                r = i - 1

            else:
                l = i + 1

    def findMedianSortedArrays3(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = nums2, nums1
        print(a, b)
        total = len(a) + len(b)
        half = total // 2
        print(total, half)

        l, r = 0, len(a)-1
        while True:
            m = (l + r) // 2
            j = half - m - 2
            aLeft = a[m] if m>=0 else float("-inf")
            aRight= a[m+1] if (m+1) >= len(a) else float("inf")
            bLeft = b[j] if j>=0 else float("-inf")
            bRight= b[j+1] if (j+1) >= len(b) else float("inf")
            print(aLeft, aRight, bLeft, bRight)

            if(aLeft <= bRight and bLeft <= aRight):
                print('correct partition')
                if total % 2 : #0 is considered as false in python
                    print("odd")
                    return min(aRight, bRight)
                else:
                    print("even")
                    ans = (max(aLeft, bLeft)+ min(aRight,bRight))/ 2
                    return ans
                break
            elif aLeft > bRight:
                print('Incorrect partition')
                print('condi#1')
                r  = m - 1
            else:
                print('Incorrect partition')
                print('condi#2')
                l = m + 1

s = Solution()
print("Answer: ", s.findMedianSortedArrays3([1,2,3,4,5,6,7,8],[1,2,3,4]))
print("Answer: ", s.findMedianSortedArrays3([1,2,3,4,5,6,7,8],[1,2,3,4,5]))
print("Answer: ", s.findMedianSortedArrays3([1,2],[3,4]))

