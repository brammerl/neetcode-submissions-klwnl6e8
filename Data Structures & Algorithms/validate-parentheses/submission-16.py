class Solution:
    def isValid(self, s: str) -> bool:
        closedBrackets = []
        closeOpen = {']': '[', '}': '{', ')': '('}

        for char in s: 
            if char in closeOpen:
                if closedBrackets and closedBrackets[-1] == closeOpen[char]:
                    closedBrackets.pop()
                else: 
                    return False
            else:
                closedBrackets.append(char)
        return True if not closedBrackets else False
