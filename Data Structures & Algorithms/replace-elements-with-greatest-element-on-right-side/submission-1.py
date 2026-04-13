class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        ans = [0] * length
        maxRight = -1

        for i in range(length - 1, -1, -1):
            ans[i] = maxRight
            maxRight = max(arr[i], maxRight)
        return ans