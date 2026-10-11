
'''
    https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=p6urvo43
'''


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = defaultdict(list)
        for s in strs:
            ar = [0]*26
            for ch in s:
                ar[ord(ch)-ord('a')] += 1
            ar = tuple(ar)
            print(ar, s)
            dic[ar].append(s)
        return dic.values()


s = Solution()


print( s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) )



