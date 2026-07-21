class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tempSet = sorted(set(nums))
        if not tempSet:
            return 0

        counter = 1
        length = 1

        for i in range(0, len(tempSet)-1):
            if tempSet[i+1] -1 == tempSet[i]:
                length += 1
            else:
                length = 1

            if length > counter:
                counter = length

        return counter