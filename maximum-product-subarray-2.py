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
this is a better solution from the perevious version of max product program.

To understand this solutions, see https://www.youtube.com/watch?v=Y6B-7ZctiW8
'''
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        i, j = 0, len(nums)-1
        ar = nums
        lv,rv=1,1 
        res = 0
        while i < len(nums):
            if lv == 0:
                lv = 1
            if rv == 0:
                rv = 1

            lv *= ar[i]
            rv *= ar[j]
            res = max(lv, rv, res)
            # print(f"{i}:{j}, {lv}, {rv}, {res}")
            j -= 1
            i += 1
        # print('result: ', res)
        return res
s = Solution()

assert s.maxProduct([-3,0,1,-2]) == 1
assert s.maxProduct([2,3,-2,-5,6, -1,4]) == 360
assert s.maxProduct([2,3,-2,4]) == 6
assert s.maxProduct([-2,0,-1]) == 0
assert s.maxProduct([-3,-1,-1]) == 3
assert s.maxProduct([-2]) == -2
assert s.maxProduct([0,2]) == 2
assert s.maxProduct([3,-1,4]) == 4
