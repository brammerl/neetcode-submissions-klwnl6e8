class Solution:
    def isValid(self, s: str) -> bool:
       openClosePairs = {')': '(', '}': '{', ']': '['}
       stack = []

       for char in s:
            if char in openClosePairs:
                if stack and stack[-1] == openClosePairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

       return True if not stack else False