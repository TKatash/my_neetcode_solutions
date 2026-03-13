from typing import List

heights = [7, 1, 7, 2, 2, 4]


def largestRectangleArea(heights: List[int]) -> int:
    stack = [-1]
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while h < heights[stack[-1]]:
            H = heights[stack.pop()]
            W = i - stack[-1] - 1
            max_area = max(max_area, H * W)
        stack.append(i)
    heights.pop()
    return max_area
