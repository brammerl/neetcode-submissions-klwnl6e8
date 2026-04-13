class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for n in nums:
            if n == 1:
                count = count + 1
            else: 
                count = 0
            res = max(res, count)
            
        return res