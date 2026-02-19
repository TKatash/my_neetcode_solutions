nums = [2, 20, 4, 10, 3, 4, 5]


def longestConsecutive(nums):
    num_set = set(nums)
    counter = 0
    max_counter = 0
    for i in num_set:
        if i - 1 not in num_set:
            while i + counter in num_set:
                counter += 1
            if counter > max_counter:
                max_counter = counter
    return max_counter


print(longestConsecutive(nums))
