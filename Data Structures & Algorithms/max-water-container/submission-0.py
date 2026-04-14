class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def waterVolume(a, b, height):
            return abs(a-b) * height
        maxVolume = 0
        for i in range(len(heights)-1):
            leftBar = heights[i]
            for j in range(i+1, len(heights)):
                rightBar = heights[j]
                maxVolume = max(maxVolume, waterVolume(i, j, min(leftBar, rightBar)))
        return maxVolume

        