class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []

        for n in nums:
            if n == val:
                continue
            else:
                ans.append(n)
        for i in range(len(ans)):
            nums[i] = ans[i]
        return len(ans)