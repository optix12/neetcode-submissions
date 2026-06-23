class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenHash = {}

        for i, num in enumerate(nums):
            val = target - num
            if val in seenHash:
                return [seenHash[val], i]
            else:
                seenHash[num] = i


        