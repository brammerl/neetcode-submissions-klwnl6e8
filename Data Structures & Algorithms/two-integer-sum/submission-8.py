class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}

        for index, num in enumerate(nums): 
            diff = target - num
            if diff in numIndex and numIndex: 
                return [numIndex[diff], index]
            else:
                numIndex[num] = index
            