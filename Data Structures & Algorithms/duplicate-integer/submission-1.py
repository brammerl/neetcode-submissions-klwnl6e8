class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}

        for number in nums: 
            if number not in hashset:
                hashset[number] = 1
            else: 
                return True
        return False