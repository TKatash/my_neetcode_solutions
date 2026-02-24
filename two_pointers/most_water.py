height = [1, 7, 2, 5, 4, 7, 3, 6]


def maxArea(nums):
    max_area = 0
    left, right = 0, len(nums) - 1
    while left < right:
        area = (right - left) * min(nums[left], nums[right])
        max_area = max(max_area, area)
        if nums[left] > nums[right]:
            right -= 1
        else:
            left += 1
    return max_area


print(maxArea(height))
