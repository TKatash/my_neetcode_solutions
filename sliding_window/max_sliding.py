from typing import List
from collections import deque

nums = [1, 2, 1, 0, 4, 2, 6]
k = 3


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    window = {}
    res = []
    left = 0
    for right, i in enumerate(nums):
        window[i] = 1 + window.get(i, 0)
        if right - left + 1 == k:
            res.append(max(window.keys()))
            window[nums[left]] -= 1
            if window[nums[left]] == 0:
                window.pop(nums[left])
            left += 1
    return res


def maxSlidingDeque(nums: List[int], k: int) -> List[int]:
    queue = deque()
    res = []
    for i, num in enumerate(nums):
        while queue and nums[queue[-1]] < num:
            queue.pop()
        queue.append(num)
        if queue[0] == i - k:
            queue.popleft()
        if i >= k - 1:
            res.append(nums[queue[0]])
    return res


print(maxSlidingWindow(nums, k))
print(maxSlidingDeque(nums, k))
