nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums):
    my_list = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            three_sum = a + nums[left] + nums[right]
            if three_sum < 0:
                left += 1
            elif three_sum > 0:
                right -= 1
            else:
                my_list.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return my_list


print(threeSum(nums))
