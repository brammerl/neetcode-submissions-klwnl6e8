class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for index, num in enumerate(nums):
            if num == 1:
                count += 1
            if num != 1 or index == len(nums) - 1: 
                res = max(count, res)
                count = 0
        return res