'''
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=oizxjoit
    https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, a in enumerate(nums):
            prev = target - a
            if prev in prevMap :
                return [prevMap[prev], i] 
            prevMap[a] = i
        return;

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))




        
