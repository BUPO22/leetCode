class Solution:
    def rob(self, nums: list[int]) -> int:
        x= len(nums)
        if x <= 2:
            return max(nums)
        
        size = [0] * x
        size[-1] = nums[-1]
        size[-2] = nums[-2]

        i = x -3

        while i >= 0:
            size[i] = max(nums[i]+ max(size[i+2:]), size[i+1])
            i -= 1

        return size[0]          

        