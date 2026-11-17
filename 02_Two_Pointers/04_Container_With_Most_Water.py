class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_cap = 0

        while left < right:
            actual_cap = (right - left) * min(height[left], height[right])
            max_cap = max(actual_cap, max_cap)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_cap