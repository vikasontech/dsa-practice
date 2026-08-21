from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_map = {}
        for i,n in enumerate(nums):
            if (n in unique_map) :
                return True
            else:
                unique_map[n] = i

        return False
         
s = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
