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
        prefix_ar = [1] * (len(nums))
        postfix_ar = [1] * (len(nums))
        res = [1] * (len(nums))
        prefix = 1
        postfix = 1
        print("input: ", nums)
        for i in range(len(nums)):
            prefix_ar[i] = prefix
            prefix *= nums[i]
        print("prefix: ", prefix_ar)
        for i in range(len(nums)-1, -1, -1):
            postfix_ar[i]=postfix * nums[i]
            postfix = postfix_ar[i]
        print("postfix: ", postfix_ar)
        # calculate result 
        for i in range(len(nums)):
            if i == 0:
                prefix = 1
                postfix = postfix_ar[1]
            elif i == len(nums)-1:
                prefix = prefix_ar[i]
                postfix = 1
            else:
                prefix = prefix_ar[i]
                postfix = postfix_ar[i+1]
            print(f"i: {i}, prefix: {prefix}, postfix: {postfix}")
            res[i]= prefix * postfix

        # print("result: ", res)
        return res
        
s = Solution()
# print(s.productExceptSelf([1,  2,  3,  4]))
# print(s.productExceptSelf([-1,1,0,-3,3]))
print(s.productExceptSelf([4,3,2,1,2]))
