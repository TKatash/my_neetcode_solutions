numbers = [1, 2, 3, 4]
target = 3


def twoSum(nums: list, target: int):
    left, right = 0, len(numbers) - 1
    while left < right and (numbers[left] + numbers[right] != target):
        if numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
    return [numbers[left], numbers[right]]


print(twoSum(numbers, target))
