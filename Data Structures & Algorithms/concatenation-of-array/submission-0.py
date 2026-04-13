class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newLen = 2 * len(nums)
        doubleArr = [0] * newLen

        for index, num in enumerate(nums): 
            doubleArr[index] = num
            doubleArr[index + len(nums)] = num

        return doubleArr
        