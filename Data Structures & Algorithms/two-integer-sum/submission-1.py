class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, number in enumerate(nums):
            diff = target - number
            if diff in numMap:
                return [numMap[diff], i]
            numMap[number] = i
        return []