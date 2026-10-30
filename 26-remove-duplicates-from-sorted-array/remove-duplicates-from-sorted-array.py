class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = []
        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] not in seen:
                seen.append(nums[fast])
                if slow != fast:
                    temp = nums[slow]
                    nums[slow] = nums[fast]
                    nums[fast] = temp
                slow += 1
            fast += 1

        ans = set(nums)

        return len(ans)

        