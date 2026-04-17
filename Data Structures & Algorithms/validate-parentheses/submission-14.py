class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       closeOpenPairs = {']': '[', '}': '{', ')': '('}
       for c in s: 
            if c in closeOpenPairs:
                if stack and stack[-1] == closeOpenPairs[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
    
       return True if not stack else False
    
