class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsdic ={}
        for i, num in enumerate(nums):
            adds = target - num
            if adds in numsdic:
                return [numsdic[adds],i]
            numsdic[num] = i
        return []
            
        