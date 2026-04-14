class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for index, n in enumerate(nums): 
            diff = target - n

            if diff not in numsDict:
                numsDict[n] = index
            else: 
                return [numsDict[diff], index]





        
        