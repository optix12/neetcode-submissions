class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        delArr = nums.copy()
        arr = []

        for i in range(k):
            maxF = max(set(delArr), key=delArr.count)
            arr.append(maxF)
            delArr = [x for x in delArr if x != maxF]

        return arr

            

        