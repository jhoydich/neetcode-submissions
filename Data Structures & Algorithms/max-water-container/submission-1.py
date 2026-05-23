class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        max_area = 0

        while start < end:
            h = min(heights[start], heights[end])
            w = end - start
            area = h * w
            if area > max_area:
                max_area = area
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        return max_area
        
        