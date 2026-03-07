from typing import List

tokens = ["1", "2", "+", "3", "*", "4", "-"]


def evalRPN(tokens: List[str]) -> int:
    stack = []
    cymbal = {"+", "-", "*", "/"}
    for i in tokens:
        if i in cymbal:
            a, b = stack[-2], stack[-1]
            stack.pop()
            stack.pop()
            if i == "+":
                stack.append(a + b)
            elif i == "-":
                stack.append(a - b)
            elif i == "*":
                stack.append(a * b)
            elif i == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(i))
    return stack[0]
