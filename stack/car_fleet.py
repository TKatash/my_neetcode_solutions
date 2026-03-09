from typing import List

target = 10
position = [1, 4]
speed = [3, 2]


def carFleet(target: int, position: List[int], speed: List[int]):
    pairs = sorted(zip(position, speed), reverse=True)
    stack = []
    for p, s in pairs:
        hours = (target - p) / s
        if stack and hours <= stack[-1]:
            continue
        else:
            stack.append(hours)
    return len(stack)
