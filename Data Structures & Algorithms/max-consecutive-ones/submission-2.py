class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0

        for index, num in enumerate(nums):
            if num == 0: 
                res = max(count, res)
                count = 0
            else: 
                count += 1
        return max(count, res)