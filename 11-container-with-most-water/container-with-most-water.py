class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) -1
        max =0
        while start < end:
            if min(height[start], height[end]) * (end - start) > max:
                max = min(height[start], height[end]) * (end - start)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max

        