def twoSum(nums, target):
    counter = {}
    for i, n in enumerate(nums):
        diff = target - n

        if diff in counter:
            return [counter[diff], i]

        counter[n] = i
