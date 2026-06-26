class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        mid = nums


        for i in range(len(nums)):
            mid.append(nums[i])
        return nums
        