class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        maximum = -1

        for i in range (n-1, -1, -1):    
            res[i] = maximum
            maximum = max(arr[i], maximum)
        return res
        


