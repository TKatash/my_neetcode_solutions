# 🦍
from typing import List

piles = [1, 4, 3, 2]
h = 9


def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    k = right
    while left <= right:
        mid = (right + left) // 2
        time = 0
        for pile in piles:
            time += (pile + mid - 1) // mid
        if time <= h:
            k = mid
            right = mid - 1
        else:
            left = mid + 1
    return k
