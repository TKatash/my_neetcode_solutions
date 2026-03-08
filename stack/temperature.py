from typing import List

temperatures = [30, 38, 30, 36, 35, 40, 28]


def dailyTemperature(temperatures: List[int]) -> List[int]:
    stack = []
    res = [0 for i in range(len(temperatures))]
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return res


print(dailyTemperature(temperatures))
