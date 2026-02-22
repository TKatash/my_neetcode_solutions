numbers = [1, 2, 3, 4]
target = 3


def twoSum(numbers: list, target: int):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return []


print(twoSum(numbers, target))
