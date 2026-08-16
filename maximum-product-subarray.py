'''
152. Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''
'''
'''
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            tx = n * curMax
            a =n * curMax
            b = n * curMin

            curMax = max(a, b, n)
            curMin = min(tx, b, n)
            res = max(res, curMax)
            print(f"{n}:: {a}, {b}, {tx}:: {curMax}, {curMin}")
        return res

s = Solution()
#
# assert s.maxProduct([2,3,-2,4]) == 6
# assert s.maxProduct([-2,0,-1]) == 0
# assert s.maxProduct([-3,-1,-1]) == 3
# assert s.maxProduct([-2]) == -2
# assert s.maxProduct([0,2]) == 2
assert s.maxProduct([3,-1,4]) == 4
