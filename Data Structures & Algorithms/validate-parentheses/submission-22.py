class Solution:
    def isValid(self, s: str) -> bool:
        closeOpen = {']': '[', '}': '{', ')': '('}
        openParenths = []

        for char in s:
            if char in closeOpen:
                if openParenths and openParenths[-1] == closeOpen[char]: 
                    openParenths.pop()
                else:
                    return False
            else:
                openParenths.append(char)
        
        print(openParenths)
        return True if not openParenths else False