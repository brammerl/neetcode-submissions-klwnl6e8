class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        sChar, tChar = {}, {}

        for i in range(len(s)):
            sChar[s[i]] = sChar.get(s[i], 0) + 1
            tChar[t[i]] = tChar.get(t[i], 0) + 1

        return sChar == tChar

