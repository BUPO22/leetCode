class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        ans =[]

        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums) -1
            while start < end:
                if nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    ans.append([nums[i],nums[start],nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    end -= 1
                    start += 1

        return ans
        