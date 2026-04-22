class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0

        for n in nums: 
            if n == 1:
                count += 1
            else:
                maximum = max(count, maximum)
                count = 0
        return max(count, maximum)
            
