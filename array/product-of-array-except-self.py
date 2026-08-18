'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
'''

'''
intuition: 

Input: nums = [1,2,3,4] ->  Output: [24,12,8,6]
Input    [1,  2,  3,  4]
prefix:  [1,  1,  2,  6]
postfix: [24, 24, 12, 4]  postFix= 1
Output:  [24, 12,  8, 6]
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix_ar = [1] * (len(nums))
        res = [1] * (len(nums))
        prefix = 1
        postfix = 1
        # print("input: ", nums)
        j = len(nums)-1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # print("prefix: ", res)
        postfix= 1
        # print("nums: ", nums) 
        for i in range(len(nums)-1, -1, -1):
            # print(f"i: {i}, postfix: {postfix}, resi: {res[i]}, numsi{nums[i]}")
            res[i]=postfix * res[i]
            postfix = postfix * nums[i]
        # print("result: ", res)
        return res
        
s = Solution()
assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
