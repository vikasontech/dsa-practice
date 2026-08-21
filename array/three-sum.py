'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=oizxjoit
'''

'''
intuition:
This problem is the combination of the problem tow-sum-II. you need to first sort the given arrary.
You cannot use 1 value twice, so you need to make sure that if previous value is already checked that skip that value. we will use pointers to trace that.

suppose the solutions is a + b + c=0. Then we need to first pick the left unique value, then use two-sum-II technic to find the correct combinations. 
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        [-1,0,1,2,-1,-4]
        [-4,-1,-1, 0, 1, 2]
        '''
        # sort the array 
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            # if a value is already checked at place `a` then don't check it again
            if i > 0 and a == nums[i-1]:
                continue;

            l, r = i +1, len(nums)-1

            while l < r: 
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -=1
                elif sum < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res;

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))


