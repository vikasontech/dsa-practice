'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''
'''
intution
'''

from typing import List

class Solution:
    def process(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        ar = nums
        while l <= r:
            mid = (l + r) // 2
            if ar[mid] == target:
                print("result: ", mid)
                return mid
            print(f"{l},{r},{mid},{ar[l]}, {ar[r]},{ar[mid]},{target}")
            if ar[l] <= ar[mid]:
                if target >= ar[l] and target < ar[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > mid and target <= ar[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        print("result: ", -1)
        return -1
s = Solution()
assert s.process([3,4,5,6,1,2], 2) == 5

# assert s.process([4,5,6,7,0,1,2], 3) == -1
# assert s.process([4,5,6,7,0,1,2], 0) == 4
# assert s.process([1,2,3,4,5,6], 6) == 5
