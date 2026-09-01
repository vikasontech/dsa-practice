'''
    https://leetcode.com/problems/combination-sum/?envType=problem-list-v2&envId=oizxjoit
'''

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        
        def dfs(i, curv, total):
            if target == total:
                res.append(curv.copy())
                return
        
            if i >= len(candidates) or total > target:
                return
            
            curv.append(candidates[i])
            dfs(i, curv, total + candidates[i])
            curv.pop()
            dfs(i + 1, curv, total)
    
        dfs(0, [], 0)
        return res

s = Solution()
print(s.combinationSum([2,3,6,7], 7))

