class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       for index, value in enumerate(nums):
        diff = target - value
        indexAhead = index + 1
        while indexAhead < len(nums):
            if nums[indexAhead] == diff:
                return [index, indexAhead]
            indexAhead += 1


        
        