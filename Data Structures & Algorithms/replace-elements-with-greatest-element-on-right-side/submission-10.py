class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        k = -1

        for i in range(n-1, -1, -1):
            res[i] = k
            k = max(arr[i], k)
        return res