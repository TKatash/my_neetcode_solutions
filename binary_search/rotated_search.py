from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Проверяем отсортирована ли левая часть
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Таргет в левой части
            else:
                left = mid + 1  # Таргет где-то в правой части

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Таргет в правой части
            else:
                right = mid - 1  # Таргет в левой части

    return -1
