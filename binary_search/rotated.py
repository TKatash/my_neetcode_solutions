from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1  # noqa: E741
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[r]
