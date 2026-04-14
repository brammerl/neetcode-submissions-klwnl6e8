class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s: 
            if char in closeToOpen:
                if store and store[-1] == closeToOpen[char]:
                    store.pop()
                else: 
                    return False
            else: 
                store.append(char)
        return True if not store else False