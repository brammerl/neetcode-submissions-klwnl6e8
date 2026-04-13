class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for index, number in enumerate(nums):
            diff = target - number

            if diff in count: 
                return [count[diff], index]
            else: 
                count[number] = index





        
        