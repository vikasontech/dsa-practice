'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

'''
'''
intution
iniput: [1,8,6,2,5,4,8,3,7] 
output: 49
'''
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        max_area = 0 

        while l < r: 
            area = (r-l) * min(height[l], height[r])
            max_area = max(max_area, area)
            # print(f"l: {l}, r:{r}, height[l]: {height[l]}, height[r]: {height[r]}, area: {area}")
            # shift poointers
    #
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1

        # print("result: ", max_area)
        return max_area

s = Solution()

assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert s.maxArea([1,1]) == 1

