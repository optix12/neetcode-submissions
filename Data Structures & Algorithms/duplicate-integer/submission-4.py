class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        fqc = {}

        for i in range(len(nums)):
            fqc[nums[i]] = 1 + fqc.get(nums[i], 0)
            if fqc[nums[i]] > 1:
                return True
        
        return False
        