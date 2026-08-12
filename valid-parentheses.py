'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

example
Input: s = "()"
Output: true
'''
'''
solution:
1. we can create a map with the pair of closing and opening brackets. to quickly get value of the corresponding opening bracket
2. use a stack, keep track of the last bracket occured, and pop it when a closing bracket found
3. is no value in input string, but the stack still have any value, then return false else return true;
'''

class Solution:
    def isValid(self, s: str) -> bool: 
        stack = []
        map = {"}":"{", ")":"(", "]": "["}
        
        for c in s:
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return false
            else:
                stack.append(c)
        
        return True if not stack else False

s = Solution()
print(s.isValid("()"))
print(s.isValid("{()"))


