class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tDict, sDict = {}, {}

        for i in range(len(s)):
            tChar = t[i]
            sChar = s[i]
            tDict[tChar] = tDict.get(tChar, 0) + 1
            sDict[sChar] = sDict.get(sChar, 0) + 1

        return tDict == sDict